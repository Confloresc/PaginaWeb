from django import forms
from .models import Producto, Imagen


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "autor",
            "titulo",
            "año",
            "descripcion",
            "tipos_de_obra",
        ]
        widgets = {
            "aprobado": forms.HiddenInput(),
            "rechazado": forms.HiddenInput(),
            "mensaje_rechazo": forms.HiddenInput(),
            "tipos_de_obra": forms.HiddenInput(),
        }


class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ["imagen"]
