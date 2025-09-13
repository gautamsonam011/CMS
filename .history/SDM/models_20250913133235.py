from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobileNumber = models.IntegerField(max_length=12)
    address = models.CharField(max_length=100)
    
class Member(models.Model):
    memName = models.CharField(max_length=20)
    jobRole = models.CharField(max_length=20)
    mobileNumber = models.IntegerField(max_length=12)
    address = models.CharField(max_length=100)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.memName}"

class GroceryProducts(models.Model):
    productName = models.CharField(max_length=70)       
    brandName = models.CharField(max_length=70)
    cost = models.FloatField(null = True)
    price = models.FloatField(null = True)
    manu_date = models.DateField(null = True)
    exp_date = models.DateField(null = True)

    
    def __str__(self):
        return f"{self.productName}"

class ProductQuantity(models.Model):
    product = models.OneToOneField(GroceryProducts, on_delete = models.CASCADE)  
    quantity = models.FloatField(null=True)
    unit = models.CharField(null=True)

    def __str__(self):
        return f"{self.unit}"

