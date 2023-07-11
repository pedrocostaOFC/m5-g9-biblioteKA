from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Book

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=127)
    username = models.CharField(unique=True, max_length=55)
    email = models.EmailField(unique=True, max_length=127)
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)

class UserBook(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
