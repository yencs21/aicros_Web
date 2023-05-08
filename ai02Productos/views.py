from django.shortcuts import render
from aicrosWeb.views import enviaste_un_email
from . import models

# Create your views here. 
def Productos(request):
    desarrollados = models.ProductosAicros.objects.all()
    distribuidos  = models.DistribuidoAicros.objects.all()

    enviaste_un_email(request)

    ctx = {
        'PaginaActual'  : "'Productos'",
        'desarrollados' :desarrollados,
        'distrubuidos'  :distribuidos,
    }
    return render(request,'Productos/Productos.html',ctx)