
from django.urls import path, include
from .views import   eliminarproducto, eliminarseguimiento, eliminarusuario, homeadmin, modUsuario, modificarproducto, modificarseguimiento, productos, crearproducto , home, registro, seguimientos, usuarios


urlpatterns = [
    path('',home, name='home'),
    path('AgregarproductoFinal.html/',crearproducto,name='crearproducto'),
    path('modificarusuario.html/<id>',modUsuario,name="modUsuario"),
    path('modificarproducto.html/<id>',modificarproducto,name="modproductos"),
    path('Gestionarusuarios.html/',usuarios,name="usuarios"),
    path('Gestionarproducto.html/',productos,name="productos"),
    path('vistAdminFinal.html/',homeadmin, name="vadmin"),
    path('Gestionarseguimiento.html/',seguimientos,name="seguimiento"),
    path('modificarseguimiento.html/<id>',modificarseguimiento,name="modificarseguimiento"),
    path('eliminarproducto.html/<id>',eliminarproducto,name="eliminarproducto"),
    path('eliminarusuario.html/<id>',eliminarusuario,name="eliminarusuario"),
    path('eliminarseguimiento.html/<id>',eliminarseguimiento,name="eliminarseguimiento"),
    path('registro.html',registro,name="registro"),






]