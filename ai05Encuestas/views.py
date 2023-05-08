from django.shortcuts import render
from aicrosWeb.views import enviaste_un_email


# Create your views here.
def Encuesta(request):

    enviaste_un_email(request)
    ctx = {
        'PaginaActual'  : "'Servicios'",
    }
    return render(request,"Encuestas/Encuestas.html",ctx)