from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):

    def __str__(self):
        return self.name

    name     = models.CharField(max_length=100)
    North    = models.FloatField()
    East     = models.FloatField()
    West     = models.FloatField()
    South    = models.IntegerField()
