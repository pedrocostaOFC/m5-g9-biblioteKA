from rest_framework import serializers

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
        copie_data = validated_data.pop("copy_id")
        user_data = validated_data["user"]
        book = Book.objects.get(id=book_data)
        loan = Loan.objects.create(**validated_data, book_id=book)  
        User.objects.filter(email=user_data).update(is_debt = "True")
        Copy.objects.filter(id=copie_data).update(is_available = "False")
        Book.objects.filter(id=book_data).update(available_copies = book.available_copies -1)

        return loan

class CreateReturnSerializer(serializers.ModelSerializer):

    user = UserLoanSerializer(read_only=True)
    
    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = ["id", "loan_date", "return_date", "is_returned", "user", "book_id"]

    def update(self, instance, validated_data):
        
        loan_data = book_data = instance.__dict__["id"]
        book_data = instance.book_id.__dict__["id"]
        user_data = instance.user
        User.objects.filter(email=user_data).update(is_debt = "False")
        Book.objects.filter(id=book_data).update(is_available = "True")
        loan = Loan.objects.filter(id=loan_data).update(is_returned = "True")

        return loan



class ListLoanSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"