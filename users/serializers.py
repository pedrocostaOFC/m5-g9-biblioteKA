from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ 'id', 'full_name', 'username', 'email', 'password', 'created_at', 'is_blocked', 'is_superuser']
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