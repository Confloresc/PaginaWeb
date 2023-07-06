from django import forms
from .models import Producto, Imagen


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            "aprobado": forms.HiddenInput(),
        }


class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ["imagen"]
