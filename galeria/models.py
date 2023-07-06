from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User


class Usuario2(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=8)

    class Meta:
        db_table = "galeria_usuario2"

    def __str__(self):
        return self.correo


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario2
        fields = ["correo", "clave"]


class FormRegistro(forms.ModelForm):
    class Meta:
        model = Usuario2
        fields = ["nombre", "apellido", "correo", "clave"]


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE).default = "text"

    def __str__(self):
        return self.nombre


class TiposDeObra(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo


class Producto(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    año = models.IntegerField(default=2023)
    categoria = models.CharField(max_length=50).default = "sin categoria"
    valor = models.DecimalField(max_digits=8, decimal_places=2).default = 999999
    descripcion = models.TextField(default="escribe una descripcion")
    tipos_de_obra = models.ManyToManyField(TiposDeObra)

    def __str__(self):
        return self.titulo


class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/imagenes")

    def __str__(self):
        return self.producto.titulo + " - Imagen " + str(self.id)
