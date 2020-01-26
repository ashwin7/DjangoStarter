from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)


class Offers(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    discount = models.FloatField()
