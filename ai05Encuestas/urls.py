from django.urls import path
from .views import Encuesta

urlpatterns = [
    path('',Encuesta,name='Encuestas'),    
] 