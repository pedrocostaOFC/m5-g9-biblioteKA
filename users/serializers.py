from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, UserBook

class UserBookSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    books = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = UserBook
        fields = '__all__'
        extra_kwargs = {'user': {"write_only": True}, 
                        'book': {"write_only": True}}

    def create(self, validated_data):
        user = self.context['request'].user
        book = validated_data['book']

        if UserBook.objects.filter(user=user, book=book).exists():
            raise serializers.ValidationError("user already follows this book.")

        user_book = UserBook.objects.create(user=user, book=book)
        return user_book

    

class UserSerializer(serializers.ModelSerializer):
    books_followed = serializers.SerializerMethodField()

    def get_books_followed(self, user):
        user_books = UserBook.objects.filter(user=user)
        return [user_book.book.title for user_book in user_books]

    class Meta:
        model = User
        fields = [ 'id', 'full_name', 'username', 'email', 'password', 'created_at', 'is_blocked', 'is_superuser', 'books_followed']
        read_only_fields = ['id']
        
        extra_kwargs = {
            'password': {"write_only": True},
            'username': {'validators': [UniqueValidator(queryset=User.objects.all(), message="username already exists.",)]},
            'email':    {'validators': [UniqueValidator(queryset=User.objects.all(), message="email already exists.",)]},
            'is_superuser': {'default': False}
        }
        

    def create(self, validated_data: dict) -> User:
        if validated_data['is_superuser']:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)
    
    
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)
         
        instance.save()
        return instance
    
class UserLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
        ]