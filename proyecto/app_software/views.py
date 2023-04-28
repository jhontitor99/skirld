from proyecto.app_software.forms import frmProducto, frmseguimiento, frmusuario
from proyecto.app_software.models import producto, seguimiento, usuario
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib import messages

# Create your views here.
def home(request) :
    return render(request,"app_software/index(cuenta registrada).html")

def homeadmin(request) :
    return render(request,"app_software/vistAdminFinal.html")

def productos(request):
    lista=producto.objects.all()

    mensaje="Lista de productos"

    contexto={
        "msg":mensaje,
        "lista":lista
    }

    return render(request,"app_software/Gestionarproducto.html",contexto)

def crearproducto(request):
    formulario=frmProducto(request.POST or None)
    contexto={
        "form":formulario
    }

    if formulario.is_valid():
        formulario.save()

        contexto={
            "mensaje":"Producto agregado"
            }



    return render(request,"app_software/AgregarproductoFinal.html",contexto)

def usuarios(request):
    lista=usuario.objects.all()
    mensaje="Lista de Usuarios"
    contexto={
        "msg":mensaje,
        "lista":lista
    }
    return render(request,"app_software/Gestionarusuarios.html",contexto)

def modUsuario(request,id):
    usuario2=get_object_or_404(usuario,idusuario=id)

    formulario=frmusuario(instance=usuario2)
    contexto={
        "form":formulario

    }
    if request.method == "POST":
        formulario=frmusuario(data=request.POST,instance=usuario2)
        if formulario.is_valid():
            usuariodb=usuario.objects.get(idusuario=usuario2.idusuario)

            datos=formulario.cleaned_data

            usuariodb.nickname=datos.get("nickname")
            usuariodb.nombre=datos.get("nombre")
            usuariodb.apellido=datos.get("apellido")
            usuariodb.email=datos.get("email")
            usuariodb.f_nacto=datos.get("f_nacto")
            usuariodb.save()

            return redirect(to="usuarios")
        contexto={
            "form":formulario,
        }
    return render(request,"app_software/modificarusuario.html " ,contexto)

def seguimientos(request):
    lista=seguimiento.objects.all()
    mensaje="Lista de seguimientos"
    contexto={
        "msg":mensaje,
        "lista":lista
    }
    return render(request,"app_software/Gestionarseguimiento.html",contexto)

def modificarproducto(request,id):
    
    producto2=get_object_or_404(producto,idproducto=id)
    formulario=frmProducto(instance=producto2)

    contexto={
        "form":formulario,
    }

    if request.method=="POST":
        formulario=frmProducto(data=request.POST,instance=producto2)
        if formulario.is_valid():
            productodb=producto.objects.get(idproducto=producto2.idproducto)

            datos=formulario.cleaned_data

            productodb.nombre=datos.get("nombre")
            productodb.modelo=datos.get("modelo")
            productodb.stock=datos.get("stock")
            productodb.precio=datos.get("precio")
            productodb.marca=datos.get("marca")
            productodb.descripcion=datos.get("descripcion")

            productodb.save()

            return redirect(to="productos")
            
        contexto={
        "form":formulario,
        }
            


    return render(request,"app_software/modificarproducto.html",contexto)

def modificarseguimiento(request,id):
    
    seguimiento2=get_object_or_404(seguimiento,idseguimiento=id)
    formulario=frmseguimiento(instance=seguimiento2)

    contexto={
        "form":formulario,
    }

    if request.method=="POST":
        formulario=frmseguimiento(data=request.POST,instance=seguimiento2)
        if formulario.is_valid():
            seguimientobd=seguimiento.objects.get(idseguimiento=seguimiento2.idseguimiento)

            datos=formulario.cleaned_data

            seguimientobd.idseguimiento=datos.get("idseguimiento")
            seguimientobd.idproducto=datos.get("idproducto")
            seguimientobd.origen=datos.get("origen")
            seguimientobd.destino=datos.get("destino")
            seguimientobd.idusuario=datos.get("idusuario")
            seguimientobd.stock=datos.get("stock")
            seguimientobd.estado_envio=datos.get("estado_envio")


            seguimientobd.save()

            return redirect(to="seguimiento")
            
        contexto={
        "form":formulario,
        }
            


    return render(request,"app_software/modificarseguimiento.html",contexto)

def eliminarproducto(request,id):
    products=get_object_or_404(producto,idproducto=id)
    datos=f"{products.nombre} -   {products.marca} -   {products.modelo} -   idproducto: {products.idproducto}"
    try:
        segui=seguimiento.objects.get(idproducto=products.idproducto)
        contexto={
        "datos":datos,
        "segui":segui
        }
    except:
        contexto={
            "datos":datos
    
    }

    if request.method=="POST":
        products.delete()
        return redirect(to="productos")


    return render(request,"app_software/eliminarproducto.html",contexto)



def eliminarusuario(request,id):
    user=get_object_or_404(usuario,idusuario=id)
    datos=f"{user.nickname} {user.nombre} {user.apellido} {user.email} {user.f_nacto} idusuario: {user.idusuario}"

    try:
        segui=seguimiento.objects.get(idusuario=user.idusuario)
        contexto={
        "datos":datos,
        "segui":segui
        }

    except:
        contexto={
        "datos":datos
        }


    

    if request.method=="POST":
        user.delete()
        return redirect(to="usuarios")

    return render(request,"app_software/eliminarusuario.html",contexto)



def eliminarseguimiento(request,id):
    segui=get_object_or_404(seguimiento,idseguimiento=id)
    datos=f"{segui.origen} - {segui.destino} - idseguimiento: {segui.idseguimiento}"

    
    contexto={
        "datos":datos
        }


    

    if request.method=="POST":
        segui.delete()
        return redirect(to="seguimiento")

    return render(request,"app_software/eliminarseguimiento.html",contexto)




def registro(request):
    form=frmusuario()
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=frmusuario(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Usuario registrado")
            return redirect(to="vadmin")
    return render(request,"registration/registro.html",contexto)