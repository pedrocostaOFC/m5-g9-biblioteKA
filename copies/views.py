from .models import Copy
from .serializers import CopySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.permissions import IsStudentOrCollaborator

class CopyView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudentOrCollaborator]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        return serializer.save(book_id=self.kwargs.get('book_id'))

class CopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    ...