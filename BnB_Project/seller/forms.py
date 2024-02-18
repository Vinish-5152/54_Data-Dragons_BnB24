from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Price', 'Quantity', 'Description', 'Image']
        Name = forms.CharField(max_length=50)
        Price = forms.IntegerField()
        Quantity = forms.IntegerField()
        Description = forms.TextInput()
        Image = forms.ImageField()
    
    def clean_Name(self):
        name = self.cleaned_data.get('Name')
        if len(name) < 3:
            raise forms.ValidationError("ENTER A VALID Product Name")
        return name