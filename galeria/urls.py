from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required


def es_admin(user):
    return user.is_authenticated and user.is_superuser


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
    path("tejido/", views.tejido, name="tejido"),
    path("tejido1/", views.tejido1, name="tejido1"),
    path("tejido2/", views.tejido2, name="tejido2"),
    path("tejido3/", views.tejido3, name="tejido3"),
    path("contacto/", views.contacto, name="contacto"),
    path("perfil/", views.perfil, name="perfil"),
    path("artistas/", views.artistas, name="artistas"),
    path("registro/", views.registro, name="registro"),
    path("productos/", views.lista_productos, name="lista_productos"),
    path("perfiladm/", views.perfil_administrador, name="perfil_administrador"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "productos/crear/",
        login_required(views.crear_producto),
        name="crear_producto",
    ),
    path(
        "productos/editar/<int:producto_id>/",
        login_required(views.editar_producto),
        name="editar_producto",
    ),
    path(
        "productos/eliminar/<int:producto_id>/",
        login_required(views.eliminar_producto),
        name="eliminar_producto",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
