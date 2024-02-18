from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Price', 'Quantity', 'Description']
        Name = forms.CharField(max_length=50)
        Price = forms.IntegerField()
        Quantity = forms.IntegerField()
        Description = forms.TextInput()