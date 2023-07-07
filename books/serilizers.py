from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id"]

        extra_kwargs = {
            "title": {
                "validators": [
                    UniqueValidator(
                        queryset=Book.objects.all(),
                        message="Book already exists.",
                    )
                ]
            },
        }
