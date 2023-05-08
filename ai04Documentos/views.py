from django.shortcuts import render
from aicrosWeb.views import enviaste_un_email
from . import models
# Create your views here. 

def Documentos(request):
    try:
        filtro = request.GET['filtrado']
    except:
        filtro =''

    print(filtro,type(filtro))
    documento   = models.Documentos.objects.all()
    contrato    = models.Contratos.objects.filter( Titulo__contains = filtro )
    servicio    = models.Servicios.objects.filter( Titulo__contains = filtro )
    catalogo    = models.Catalogos.objects.filter( Titulo__contains = filtro )
    otro        = models.Otros.objects.filter( Titulo__contains = filtro )

    enviaste_un_email(request)
    data = [len(contrato),len(servicio),len(catalogo),len(otro)]
    vacio = 0
    for i in data:
        if i == 0: vacio += 1
    ctx = {
        'PaginaActual'  : "'Documentos'",
        'data'          : data      ,
        'columnajs'     : 0         ,
        'documento'     : documento ,
        'contrato'      : contrato  ,
        'servicio'      : servicio  ,
        'catalogo'      : catalogo  ,
        'otro'          : otro      ,
        'filtro'        : filtro    ,
        'vacio'         : vacio     ,
    }
    return render(request,"Documentos/Documentos.html",ctx)