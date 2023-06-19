from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "galeria/index.html", {})

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

