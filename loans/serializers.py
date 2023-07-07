from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User
from books.models import Book
from loans.models import Loan
from copies.models import Copy

from books.serializers import BookSerializer
from users.serializers import UserSerializer, UserLoanSerializer

class ListLoanSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"

        
class CreateLoanSerializer(serializers.ModelSerializer):

    user = UserLoanSerializer(read_only=True)

    
    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = ["user_id", "copy_id", "loan_date", "return_date", "was_returned", ]


    def create(self, validated_data):
        book_data = validated_data.pop("book_id")
        # copie_data = validated_data.pop("copy_id")
        user_data = validated_data["user_id"]
        user = User.objects.get(id=user_data)
        book = Book.objects.get(id=book_data)
        loan = Loan.objects.create(**validated_data, book_id=book)
        # User.objects.
        Copy.objects.filter(id=validated_data.copy_id).update(is_avaiable = "False")
        Book.objects.filter(id=book_data).update(avaiable_copies = book.avaiable_copies -1)


        return loan

class CreateReturnSerializer(serializers.ModelSerializer):

    user = UserLoanSerializer(read_only=True)
    
    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = ["id", "loan_date", "return_date", "is_returned", "user", "book_id", "copy_id"]

    def update(self, instance, validated_data):
        
        loan_data = book_data = instance.__dict__["id"]
        book_data = instance.book_id.__dict__["id"]
        user_data = instance.user
        Copy.objects.filter(id=book_data).update(is_avaiable = "True")
        loan = Loan.objects.filter(id=loan_data).update(is_returned = "True")

        return loan



class ListLoanSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"