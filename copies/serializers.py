from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer

class CopySerializer(serializers.ModelSerializer):

    book = BookSerializer(read_only=True)
    
    class Meta:
        model = Copy
        fields = [
            'id',
            'is_avaiable',
            'book'
        ]