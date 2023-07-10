from rest_framework import generics
from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from loans.mixins import SerializerMethodMixin
from loans.permissions import IsOwnerOrAdmin, IsDebitoAndAvailable, IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication

from datetime import timedelta, date
from django.utils import timezone


from loans.models import Loan
from users.models import User
from copies.models import Copy

from loans.serializers import ListLoanSerializer, CreateLoanSerializer, CreateReturnSerializer
    
class ListCreateLoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Loan.objects.all()

    serializer_class = CreateLoanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        instance_user = get_object_or_404(User, pk=self.request.user.id)

        return queryset.filter(user=instance_user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, copy_id=self.request.data["copy_id"])

class LoanDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Loan.objects.all()

    serializer_class = CreateLoanSerializer

    def patch(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.data["user_id"])
        copy = Copy.objects.get(id=self.request.data["copy_id"])

        now = timezone.now().date()

        date_return = Loan.return_date
        block_end_date = now + timedelta(days=3)

        if not user.is_blocked:
                user.is_blocked = True
                user.block_end_date = block_end_date
                user.save()

        loan_date = user.objects.filter(user=user, is_blocked=False).exists()

        if not loan_date:
                additional_block_days_after_return = 5
                user.block_end_date += timedelta(days=additional_block_days_after_return)
                user.save()

        # if now > date_return:

        return Response({"message": "This user cannot borrow any books for at least 5 more days"})

        copy.is_available = True
        copy.save()

        return self.partial_update(request, *args, **kwargs)