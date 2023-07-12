from rest_framework import generics
from rest_framework.views import status
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import date
from loans.models import Loan
from users.models import User
from copies.models import Copy
from books.models import Book
from .permissions import IsCollaborator
from loans.serializers import CreateLoanSerializer
from rest_framework.exceptions import APIException

class ListCreateLoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Loan.objects.all()
    serializer_class = CreateLoanSerializer

    def perform_create(self, serializer):
        copy_id = self.request.data.get("copy_id")
        user_id = self.request.data.get("user_id")
        if not copy_id or not user_id:
            raise APIException("Copy ID and User ID must be provided.", code=status.HTTP_400_BAD_REQUEST)
        copy = get_object_or_404(Copy, pk=copy_id)
        user = get_object_or_404(User, pk=user_id)
        book = get_object_or_404(Book, pk= copy.book.id)
        if user.is_blocked:
            raise APIException("User is blocked.", code=status.HTTP_403_FORBIDDEN)
        if book.avaiable_copies > 0:
            book.avaiable_copies -= 1
            book.save()
        else:
            raise APIException("No more copies available.", code=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=user, copy=copy)


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
            raise APIException({"message": "You must return the book."}, status.HTTP_400_BAD_REQUEST)
        return self.partial_update(request, *args, **kwargs)