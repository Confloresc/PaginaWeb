from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),  
    path("loginForm/", views.loginForm, name="loginForm"), 
    path("categoria/", views.categoria, name="categoria"), 
    path("pinturas/", views.pinturas, name="pinturas"),
    path("pintura1/", views.pintura1, name="pintura1"),
    path("pintura2/", views.pintura2, name="pintura2"),
    path("pintura3/", views.pintura3, name="pintura3"),
    path("esculturas/", views.esculturas, name="esculturas"),
    path("escultura1/", views.escultura1, name="escultura1"),
    path("escultura2/", views.escultura2, name="escultura2"),
    path("escultura3/", views.escultura3, name="escultura3"),
    path("orfebreria/", views.orfebreria, name="orfebreria"),
    path("anillos/", views.anillos, name="anillos"),
    path("aretes/", views.aretes, name="aretes"),
    path("collar/", views.collar, name="collar"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
