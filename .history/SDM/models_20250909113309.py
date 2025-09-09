from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobileNumber = models.IntegerField(max_length=12)
    address = models.CharField(max_length=100)
    