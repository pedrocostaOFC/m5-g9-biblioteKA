from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from loans.models import Loan

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=127)
    username = models.CharField(unique=True, max_length=55)
    email = models.EmailField(unique=True, max_length=127)
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)

    def check_if_blocked(self):
        loans = Loan.filter(was_returned=False)
        today = timezone.now().date()
        days_without_weekends = 0

        for loan in loans:
            loan_date = loan.loan_date.date()
            delta = today - loan_date

     
            for i in range(delta.days + 1):
                current_date = loan_date + timedelta(days=i)
                if current_date.weekday() < 5:
                    days_without_weekends += 1

        if days_without_weekends >= 30:
            self.is_blocked = True
            self.save()

class UserBook(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
