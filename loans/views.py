from rest_framework import generics
from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from loans.mixins import SerializerMethodMixin
from loans.permissions import IsOwnerOrAdmin, IsDebitoAndAvailable, IsAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication


from loans.models import Loan
from users.models import User

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



class RetrieveLoanView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Loan
    serializer_class = ListLoanSerializer

    
class DeletedLoanView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    queryset = Loan
    serializer_class = ListLoanSerializer     