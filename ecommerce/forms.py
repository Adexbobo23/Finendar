from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'discounted_price', 'category', 'main_image', 'image1', 'image2', 'image3', 'image4', 'video', 'stock', 'available']
