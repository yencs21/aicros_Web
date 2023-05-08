from django.urls import path
from .views import Servicios,Categoria_view


urlpatterns = [
    path('',Servicios,name='Servicios'),
    path('Categorias/<int:categoria_id>/',Categoria_view,name='Categoria')
] 