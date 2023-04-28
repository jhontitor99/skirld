from django.db import models
from django.db.models.deletion import PROTECT,CASCADE
from django.db.models.fields import CharField
from django.utils.timezone import now

# Create your models here.

class producto(models.Model):
    idproducto=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    modelo=models.CharField(max_length=50)
    stock=models.IntegerField(default="0")
    precio=models.IntegerField()
    marca=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=2000)
    def __str__(self):
        return f"{self.idproducto} - {self.nombre} - {self.marca} - {self.modelo}- {self.stock}"
class usuario(models.Model):
        idusuario=models.AutoField(primary_key=True)
        nickname=models.CharField(max_length=20)
        nombre=models.CharField(max_length=50)
        apellido=models.CharField(max_length=50)
        email=models.CharField(max_length=50)
        f_nacto=models.DateField(auto_now=False)
        def __str__(self):
            return f"{self.idusuario} - {self.nickname} - {self.nombre} - {self.apellido} - {self.email}- {self.f_nacto}"

class seguimiento(models.Model):
        idseguimiento=models.AutoField(primary_key=True)
        idproducto=models.ForeignKey(producto,on_delete=PROTECT,default="0",related_name='idproducto_sk')

        origen=models.CharField(max_length=200)
        destino=models.CharField(max_length=50)
        idusuario=models.ForeignKey(usuario,on_delete=PROTECT,default="0",related_name='idusuario_sk')
        stock=models.ForeignKey(producto,on_delete=PROTECT,default="0", related_name='stock_sk')
        estado_envio=models.CharField(max_length=10)
        def __str__(self):
            return f"{self.idseguimiento} - {self.idproducto} - {self.origen} - {self.destino} - {self.stock}- {self.estado_envio}"
            