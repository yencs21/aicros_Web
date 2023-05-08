from django.shortcuts import render
from aicrosWeb.views import enviaste_un_email
from . import models
from aicrosWeb.models import a4Negocio
# Create your views here. 

def Servicios(request):
    servicios = models.Servicios.objects.all()
    categoia  = a4Negocio.objects.all()
    
    enviaste_un_email(request)

    ctx = {
        'PaginaActual'  : "'Servicios'",
        'categorias'    : categoia,
        'servicios'     : servicios,
    }
    return render(request,"Servicios/Servicios.html",ctx)

#Esta vista se elimino pues ya no es necesaria se, se sustitullo por una funcion javaScript.
''''''
def Categoria_view( request , categoria_id ):
    print(categoria_id,'categoria ID')
    categoria           = a4Negocio.objects.get(id = categoria_id)
    categoria_completa  = a4Negocio.objects.all()
    servicios           = models.Servicios.objects.filter( Categoria = categoria ) 

    enviaste_un_email(request)    
    ctx = { 
        'categorias'    : categoria_completa,
        'servicios'     : servicios,
        'categoria_id'  : categoria,
        }
    
    return render(request,"Servicios/Categoria.html",ctx)
