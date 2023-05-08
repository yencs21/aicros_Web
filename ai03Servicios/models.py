from django.db import models
from aicrosWeb.models import a4Negocio

# Create your models here.

class Servicios(models.Model):
    Servicio    = models.TextField(max_length=500)
    Iconos      = models.ImageField()
    Categoria   = models.ForeignKey( a4Negocio, on_delete=models.CASCADE )

    class Meta:
        verbose_name = '01Servicio'
        verbose_name_plural = '01Servicios'

    def __str__(self):
        return self.Servicio