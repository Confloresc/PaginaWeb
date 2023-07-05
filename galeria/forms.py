from django import forms
from .models import Producto, Imagen

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        imagen = forms.ImageField()
        fields = '__all__'

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen']
        
