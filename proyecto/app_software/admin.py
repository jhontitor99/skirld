from models import producto, seguimiento, usuario
from django.contrib import admin
from typing import ClassVar

# Register your models here.
class AdmProducto(admin.ModelAdmin):
    list_display=["idproducto","nombre","modelo","stock","precio","marca","descripcion"]
    list_editable=["nombre","modelo","stock","precio","marca","descripcion"]
class Meta:
    model=producto
admin.site.register(producto,AdmProducto)

class AdmUsuario(admin.ModelAdmin):
    list_display=["idusuario","nickname","nombre","apellido","email","f_nacto"]
    list_editable=["nickname","nombre","apellido","email","f_nacto"]
class Meta:
    model=usuario
admin.site.register(usuario,AdmUsuario)

class Admseguimiento(admin.ModelAdmin):
    list_display=["idseguimiento","idproducto","origen","destino","idusuario","stock","estado_envio"]
    list_editable=["origen","destino","estado_envio"]
class Meta:
    model=seguimiento
admin.site.register(seguimiento,Admseguimiento)