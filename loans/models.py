from datetime import datetime, timedelta
from django.db import models

def return_date():    
    return datetime.now() + timedelta(days=30)

class Loan(models.Model):
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=return_date)
    is_returned = models.BooleanField(default=False) 
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loan"
    ) 
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.PROTECT, related_name="copy"
    )
