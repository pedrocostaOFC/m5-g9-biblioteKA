from datetime import datetime, timedelta, date
from django.db import models
from django.utils import timezone

def return_date():    
    return datetime.now() + timedelta(days=31)



class Loan(models.Model):
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    was_returned = models.BooleanField(default=False) 
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loan"
    ) 
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="loan"
    )

    def save(self, *args, **kwargs):
        if not self.return_date:
            self.return_date = self.calculate_return_date()
        super().save(*args, **kwargs)

    def calculate_return_date(self):
        loan_date = self.loan_date.date() if self.loan_date else timezone.now().date()
        days_added = 0

        while days_added < 31:
            loan_date += timedelta(days=1)
            if loan_date.weekday() < 5:
                days_added += 1

        return timezone.make_aware(datetime.combine(loan_date, datetime.min.time()))