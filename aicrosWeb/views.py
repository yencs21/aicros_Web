from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    promocion = models.a1Promociones.objects.all()
    productos = models.a2Productos.objects.all()
    servicos  = models.a3Servicios.objects.all()
    negocios  = models.a4Negocio.objects.all()
    sifras    = models.a5Sifras.objects.all()
    noticias  = models.a6Noticias.objects.all()
    alianzas  = models.a7Alianzas.objects.all()

    enviaste_un_email(request)
    
    ctx = { 
        'PaginaActual'  : "'Home'",
        'promocion' : promocion ,
        'productos'  : productos ,
        'servicios'  : servicos ,
        'negocios'   : negocios ,
        'sifras'     : sifras ,
        'noticias'   : noticias,
        'alianzas'   : alianzas,
        }
    return render(request,'Home/home.html',ctx)


def enviaste_un_email(request):

    if request.method == "POST":

        asunto          = request.POST['Nombre'] +'('+ request.POST['Personalidad'] +')'
        contenido       = request.POST['Contenido'] + ' ' + request.POST['Correo']
        remitente       = request.POST['Correo']
        destinatario    = settings.EMAIL_HOST_USER
        
        #  send_mail( asunto, contenido, destinatario, [ remitente ], fail_silently = False, )
        send_mail( asunto, contenido, remitente, [ destinatario ], fail_silently = False )
