from django.db import models
from taggit.managers import TaggableManager
from verifier.models import Verifier_Profile

# Create your models here.


class Seller_Profile(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50)
    Is_Email_Verified = models.BooleanField(default=False)
    Phone_Number = models.CharField(max_length=10)
    Is_Phone_Number_Verified = models.BooleanField(default=False)
    Password = models.CharField(max_length=175)

    def __str__(self):
        if self.Last_Name:
            return self.First_Name + " " + self.Last_Name
        else:
            return self.First_Name
        

class Category(models.Model):
    Name = models.CharField(max_length=15)

    def _str_(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Price = models.IntegerField(null=False, blank=False)
    Is_Product_Verified = models.BooleanField(default=False)
    Product_Verified_By = models.ForeignKey(Verifier_Profile, on_delete=models.CASCADE, default=1)
    Quantity = models.IntegerField(null=False, blank=False)
    Description = models.TextField(null=False, blank=False)

    def _str_(self):
        return self.Name