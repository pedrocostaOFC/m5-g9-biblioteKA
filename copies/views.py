from .models import Copy
from .serializers import CopySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.views import Response, status
from .permissions import IsCollaborator
from books.models import Book
from django.shortcuts import get_object_or_404

class CopyView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        book = Book.objects.get_object_or_404(Book, id=self.request.book_id)

        book.avaiable_copies = avaiable_copies + 1

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save(book_id=self.request.book_id)

class CopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer