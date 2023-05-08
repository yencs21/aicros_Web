from django.db import models

# Create your models here. 
class ProductosAicros(models.Model):
    Titulo      = models.CharField(max_length=100)
    Contenido   = models.TextField(max_length=5000)
    Desarrollo  = models.ImageField()
    Logotipo    = models.ImageField()

    class Meta:
        verbose_name        = '01Desarrollado'
        verbose_name_plural = '01Desarrollados'

    def __str__(self):
        return self.Titulo

class DistribuidoAicros(models.Model):
    Titulo      = models.CharField(max_length=100)
    Contenido   = models.TextField(max_length=5000)
    Desarrollo  = models.ImageField()
    Logotipo    = models.ImageField()

    class Meta:
        verbose_name        = '02Distribuido'
        verbose_name_plural = '02Distribuidos'

    def __str__(self):
        return self.Titulo