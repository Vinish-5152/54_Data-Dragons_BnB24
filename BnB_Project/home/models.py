from django.db import models

# Create your models here.

class Customer(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50)
    Is_Email_Verified = models.BooleanField(default=False)
    Phone_Number = models.CharField(max_length=10)
    Is_Phone_Number_Verified = models.BooleanField(default=False)
    Password = models.CharField(max_length=175)
    User_Type = models.CharField(max_length=10, default='Customer', choices=(('Customer', 'Customer'), ('Seller', 'Seller'), ('Verifier', 'Verifier')))

    def __str__(self):
        if self.Last_Name:
            return self.First_Name + " " + self.Last_Name
        else:
            return self.First_Name
