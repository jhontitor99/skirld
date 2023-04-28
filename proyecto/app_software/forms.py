from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Widget
from .models import producto, seguimiento, usuario
from django import forms

class frmProducto(forms.ModelForm):
    #nombre: forms.TextInput(attrs={"'class':'form-control'"})
    #modelo: forms.TextInput(attrs={'class':'form-control'})
    #stock: forms.Select(attrs={'class':'form-control'})
    #precio: forms.TextInput(attrs={'class':'form-control'})
    #marca: forms.TextInput(attrs={'class':'form-control'})
    #descripcion: forms.Textarea(attrs={'class':'form-control'})

    
    class Meta:
        model=producto
        
        fields=["idproducto","nombre","modelo","stock","precio","marca","descripcion"]
       
        
        
class frmusuario(forms.ModelForm):
    
    f_nacto=forms.DateField(label="Fecha de Nacimiento",widget=forms.TextInput(attrs={"type":"date"}))

    class Meta:
        model=usuario
        fields=["idusuario","nickname","nombre","apellido","email","f_nacto"]

class frmseguimiento(forms.ModelForm):
    
    
    class Meta:
        model=seguimiento
        fields=["idseguimiento","idproducto","origen","destino","idusuario","stock","estado_envio"]
