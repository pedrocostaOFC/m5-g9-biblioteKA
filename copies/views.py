from django.shortcuts import get_object_or_404
from .models import Copy
from .serializers import CopySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsCollaborator
from books.models import Book

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


        book_id = request.data["book_id"]
        book = get_object_or_404(Book, pk=book_id)
        if not book.avaiable_copies:
            book.avaiable_copies = 1
        else:  
            book.avaiable_copies += 1 
             
        book.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(book_id=self.request.data["book_id"])


class CopyDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer