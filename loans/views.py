from rest_framework import generics
from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from datetime import timedelta, date
from django.utils import timezone


from loans.models import Loan
from users.models import User
from copies.models import Copy
from books.models import Book

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

        if request.data["was_returned"] == True:

            now_date = date.today()
            loan = get_object_or_404(Loan, id=self.kwargs.get('pk')) 
            return_date = loan.return_date.date()
            copy = get_object_or_404(Copy, id=loan.copy.id)
            copy.is_avaiable = True
            book = get_object_or_404(Book, id=copy.book_id)
            book.avaiable_copies += 1
            copy.save()
            book.save()

            if now_date > return_date:
                user = get_object_or_404(User, pk=loan.user.id)
                user.is_blocked = True
                user.save()
        
        else:
            return Response({"message": "You must return the book."}, status.HTTP_400_BAD_REQUEST)

        return self.partial_update(request, *args, **kwargs)