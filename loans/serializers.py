from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User
from books.models import Book
from loans.models import Loan
from copies.models import Copy
from books.serializers import BookSerializer
from users.serializers import UserSerializer, UserLoanSerializer

class CreateLoanSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ["id", "user", "copy_id", "return_date", "loan_date", "was_returned"]
        read_only_fields = ["user_id", "copy_id", "return_date", "loan_date", "was_returned"]

        def create(self, validated_data):
            return Loan.objects.create(**validated_data)
        

class CreateReturnSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = ["user_id", "copy_id", "loan_date", "return_date", "was_returned"]

    def update(self, instance, validated_data):
        instance.was_returned = True
        instance.copy.is_available = True
        instance.copy.save()
        instance.save()
        return instance

class ListLoanSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"