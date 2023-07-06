from django.db import models

class Copy(models.Model):
    class Meta:
        ordering = ['id']
    
    is_avaiable = models.BooleanField(default=True)

    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        related_name='copy',
    )