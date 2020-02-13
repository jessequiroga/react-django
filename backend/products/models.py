from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    descriptions = models.TextField()
    price = models.CharField(max_length=25)
    status = models.BooleanField(default=False)