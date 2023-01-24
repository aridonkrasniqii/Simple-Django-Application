from django.db import models


# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField(default='This is my model that i\'ve created')
    description = models.TextField(default='Description')

    def __str__(self):
        return self.title
