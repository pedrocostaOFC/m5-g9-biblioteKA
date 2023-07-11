from datetime import datetime, timedelta, date
from django.db import models
from django.utils import timezone

def return_date():    
    date = datetime.now() + timedelta(days=30)
    
    while date.weekday() >= 5:
        date += timedelta(days=1)

    return date


class Loan(models.Model):
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=return_date)
    was_returned = models.BooleanField(default=False) 
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loan"
    ) 
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="loan"
    )