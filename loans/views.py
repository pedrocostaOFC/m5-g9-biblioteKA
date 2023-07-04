from rest_framework import generics
from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from loans.mixins import SerializerMethodMixin
from loans.permissions import IsOwnerOrAdmin, IsDebitoAndAvailable, IsAdmin

from loans.models import Loan

from loans.serializers import ListLoanSerializer, CreateLoanSerializer, CreateReturnSerializer
    
class ListCreateLoanView(SerializerMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsDebitoAndAvailable]

    queryset = Loan.objects.all()          
    serializer_map = {
        'GET': ListLoanSerializer,
        'POST': CreateLoanSerializer,
    }         

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, book_id=self.request.data["book_id"])



class UpdateReturnView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdmin]

    queryset = Loan.objects.all()          
    serializer_class = CreateReturnSerializer         



class RetrieveLoanView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Loan
    serializer_class = ListLoanSerializer

    
class DestroyLoanView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    queryset = Loan
    serializer_class = ListLoanSerializer     