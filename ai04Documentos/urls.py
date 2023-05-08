from django.urls import path
from .views import Documentos
 
urlpatterns = [
    path('',Documentos,name='Documentos'), 
] 