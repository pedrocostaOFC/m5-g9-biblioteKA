from .models import User, UserBook
from .serializers import UserSerializer, UserBookSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsStudentOrCollaborator


# Create your views here.

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudentOrCollaborator]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserBookViewDetail(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudentOrCollaborator]

    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer

class UnfollowBookView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudentOrCollaborator]

    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer