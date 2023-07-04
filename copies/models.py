from django.db import models

class Copy(models.Model):
    class Meta:
        ordering = ['id']
    
    is_avaiable = models.BooleanField(default=True)