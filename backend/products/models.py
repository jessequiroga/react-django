from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    descriptions = models.TextField()
    price = models.TextField()
    status = models.BooleanField(default=False)