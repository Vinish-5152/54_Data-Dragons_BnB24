from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=15)

    def _str_(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=50)
    # Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Price = models.IntegerField(null=False, blank=False)
    Quantity = models.IntegerField(null=False, blank=False)
    Description = models.TextField(null=False, blank=False)

    def _str_(self):
        return self.Name