from django.shortcuts import render
from aicrosWeb.views import enviaste_un_email
from . import models
# Create your views here. 
def Nosotros(request):
    valores     = models.Valores.objects.all()
    historia    = models.Historia.objects.all()
    cronologia  = models.Cronologia.objects.all()
    equipo      = models.Equipo.objects.all()
    valoresfin  = models.ValoresFinal.objects.all()

    enviaste_un_email(request)
    
    ctx = { 
        'PaginaActual'  : "'Nosotros'",
        'valores'     : valores,
        'historias'   : historia,
        'cronologias' : cronologia,
        'equipos'     : equipo,
        'valoresfin'  : valoresfin, }
    
    return render(request,'Nosotros/Nosotros.html',ctx)