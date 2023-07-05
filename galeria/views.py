from django.shortcuts import render, redirect
from .models import UsuarioForm, FormRegistro, Producto, Imagen
from .forms import ProductoForm, ImagenForm




def index(request):
    return render(request, "galeria/index.html", {})

def login(request):
     if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
     else:
        form = UsuarioForm()
     return render(request, "galeria/login.html", {'form': form})

def registro(request):
    form = FormRegistro()
    if request.method == 'POST':
        print("error 1 ",form.errors)
        form = FormRegistro(request.POST)
        if form.is_valid():
            form.save()
            print("error 2 ",form.errors)
            return redirect('index')
    else:
        form = FormRegistro()
        print("error 3 ",form.errors)
    print("error 4 ",form.errors)
    return render(request, "galeria/registro.html", {"form": form})


def loginForm(request):
    return render(request, "galeria/index.html", {})

def categoria(request):
    return render(request, "galeria/categoria.html", {})

def pinturas(request):
    return render(request, "galeria/pinturas/pinturas.html", {})

def pintura1(request):
    return render(request, "galeria/pinturas/pintura1.html", {})

def pintura2(request):
    return render(request, "galeria/pinturas/pintura2.html", {})

def pintura3(request):
    return render(request, "galeria/pinturas/pintura3.html", {})

def esculturas(request):
    return render(request, "galeria/esculturas/esculturas.html", {})

def escultura1(request):
    return render(request, "galeria/esculturas/escultura1.html", {})

def escultura2(request):
    return render(request, "galeria/esculturas/escultura2.html", {})

def escultura3(request):
    return render(request, "galeria/esculturas/escultura3.html", {})

def orfebreria(request):
    return render(request, "galeria/orfebreria/orfebreria.html", {})

def anillos(request):
    return render(request, "galeria/orfebreria/anillos.html", {})

def aretes(request):
    return render(request, "galeria/orfebreria/aretes.html", {})

def collar(request):
    return render(request, "galeria/orfebreria/collar.html", {})
    
def tejido(request):
    return render(request, "galeria/tejido/tejido.html", {})

def tejido1(request):
    return render(request, "galeria/tejido/tejido1.html", {})

def tejido2(request):
    return render(request, "galeria/tejido/tejido2.html", {})    
    
def tejido3(request):
    return render(request, "galeria/tejido/tejido3.html", {})

def contacto(request):
    return render(request, "galeria/contacto.html", {})

def perfil(request):
    return render(request, "galeria/perfil.html", {})

def artistas(request):
    return render(request, "galeria/artistas.html", {})



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'galeria/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            imagenes = request.FILES.getlist('imagenes')
            for imagen in imagenes:
                Imagen.objects.create(producto=producto, imagen=imagen)
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'galeria/crear_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            imagenes = request.FILES.getlist('imagenes')
            Imagen.objects.filter(producto=producto).delete()
            for imagen in imagenes:
                Imagen.objects.create(producto=producto, imagen=imagen)
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'galeria/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'galeria/eliminar_producto.html', {'producto': producto})

