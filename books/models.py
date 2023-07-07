from django.db import models


class Book(models.Model):
    class Meta:
        ordering = "id"

    title = models.CharField(max_length=55, unique=True)
    category = models.CharField(max_length=20)
    author = models.CharField(max_length=55)
    pages = models.IntegerField()
    synopsis = models.TextField()
    avaiable_copies = models.IntegerField(null=True)
