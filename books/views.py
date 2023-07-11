from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsStudentOrCollaborator

# Create your views here.


class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudentOrCollaborator]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


