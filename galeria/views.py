from audioop import reverse
from imaplib import _Authenticator
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .models import UsuarioForm, FormRegistro, Producto, Imagen, Usuario2
from .forms import ProductoForm, ImagenForm
from django.contrib.auth import login as auth_login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


global user


def index(request):
    # Tu lógica de vista aquí

    # Pasar el usuario autenticado en el contexto
    context = {"user": request.user}

    return render(request, "galeria/index.html", context)


def login(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

    else:
        form = UsuarioForm()
    return render(request, "galeria/login.html", {"form": form})


def loginForm(request):
    form = UsuarioForm(request.POST)
    if form.is_valid():
        correo = form.cleaned_data["correo"]
        clave = form.cleaned_data["clave"]

        # Inicializar las variables de usuario
        usuario_auth = None
        usuario_personalizado = None

        # Buscar un usuario en ambas tablas
        try:
            usuario_auth = User.objects.get(email=correo)
            usuario_personalizado = Usuario2.objects.get(correo=correo)
        except User.DoesNotExist:
            usuario_auth = None
        except Usuario2.DoesNotExist:
            usuario_personalizado = None

        # Autenticar al usuario según la tabla correspondiente
        if usuario_auth and usuario_auth.check_password(clave):
            # Usuario encontrado en la tabla de usuarios autenticados (auth_user)
            # Autenticar al usuario y realizar el inicio de sesión
            user = authenticate(request, username=usuario_auth.username, password=clave)
            if user is not None:
                auth_login(request, user)
                return redirect("index")
        elif usuario_personalizado is not None and usuario_personalizado.clave == clave:
            # Usuario encontrado en la tabla personalizada (Usuario2)
            # Autenticar al usuario y realizar el inicio de sesión
            user = Usuario2.objects.get(correo=correo)
            auth_login(request, user)
            return redirect("index")

        # Credenciales inválidas, mostrar un mensaje de error
        error_message = "Credenciales inválidas, por favor intenta nuevamente."
        return render(
            request,
            "galeria/login.html",
            {"form": form, "error_message": error_message},
        )
    else:
        form = UsuarioForm()
        return render(request, "galeria/login.html", {"form": form})


def registro(request):
    form = FormRegistro()
    if request.method == "POST":
        print("error 1 ", form.errors)
        form = FormRegistro(request.POST)
        if form.is_valid():
            form.save()
            print("error 2 ", form.errors)
            return redirect("index")
    else:
        form = FormRegistro()
        print("error 3 ", form.errors)
    print("error 4 ", form.errors)
    return render(request, "galeria/registro.html", {"form": form})


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


def perfil_administrador(request):
    return render(request, "galeria/perfil_administrador.html", {})


@login_required(login_url="login")
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "galeria/lista_productos.html", {"productos": productos})


@login_required(login_url="login")
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)

            if not request.user.is_superuser:
                Usuario2 = get_user_model()
                usuario2 = Usuario2.objects.get(correo=request.user.email)
                producto.autor = usuario2
                producto.email_autor = request.user.email

            producto.save()

            imagenes = request.FILES.getlist("imagenes")
            for imagen in imagenes:
                Imagen.objects.create(producto=producto, imagen=imagen)

            return redirect("productos")
    else:
        form = ProductoForm()

    return render(request, "galeria/crear_producto.html", {"form": form})


@login_required(login_url="login")
def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            imagenes = request.FILES.getlist("imagenes")
            Imagen.objects.filter(producto=producto).delete()
            for imagen in imagenes:
                Imagen.objects.create(producto=producto, imagen=imagen)
            return redirect("productos")
    else:
        form = ProductoForm(instance=producto)
    return render(
        request, "galeria/editar_producto.html", {"form": form, "producto": producto}
    )


@login_required(login_url="login")
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect("productos")
    return render(request, "galeria/eliminar_producto.html", {"producto": producto})


def logout_view(request):
    logout(request)
    return redirect("index")
