from django.urls import path
from .views import Nosotros
#path de nuestras url
urlpatterns = [
    path('',Nosotros,name='Nosotros'),
] 