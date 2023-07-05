from django.contrib import admin
from .models import Autor, TiposDeObra, Producto, Imagen

class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 0

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenInline]

admin.site.register(Autor)
admin.site.register(TiposDeObra)
admin.site.register(Producto, ProductoAdmin)
