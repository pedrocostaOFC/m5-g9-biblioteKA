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




class UpdatedReturnView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdmin]

    queryset = Loan.objects.all()          
    serializer_class = CreateReturnSerializer         



class RetrieveLoanView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Loan.objects.all()
    serializer_class = ListLoanSerializer

    def patch(self, request):
        try:
            copy = Copy.objects.get(id=request.data["copy_id"])
        except:
            return Response(
                {"message": "Copy does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            loan = Loan.objects.get(
                user=self.request.user, copy=copy, return_date=None
            )
        except:
            return Response(
                {"message": "the book is still within the return date."},
                status=status.HTTP_404_NOT_FOUND,
            )

        loan.return_date = timezone.now()
        copy.is_avaiable = False

        if loan.return_date > loan.loan_date:
            user = self.request.user
            user.is_blocked = True
            if (loan.return_date - loan.loan_date) > timedelta(day=1):
                violated_days = loan.return_date - loan.loan_date
                punishment = (violated_days * 2) + 7
                user.blocked_until = timedelta(days=punishment)
            else:
                user.blocked_until = timezone.now() + timedelta(days=7)
            user.save()

        loan.save()
        copy.save()

        return Response({"message": "Book returned."}, status=status.HTTP_200_OK)


    
class DeletedLoanView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    queryset = Loan
    serializer_class = ListLoanSerializer 