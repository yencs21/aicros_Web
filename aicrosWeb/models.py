from django.db import models

# Create your models here.
class a1Promociones(models.Model):
    Titulo      = models.CharField(max_length=50)
    Contenido   = models.TextField(max_length=500)
    imagen      = models.ImageField(upload_to="Home/Promociones",null=True,blank=True,)
    Creado      = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = '01Promocion'
        verbose_name_plural = '01Promociones'
    
    def __str__(self):
        return self.Titulo

class a2Productos(models.Model):
    Titulo      = models.CharField(max_length=50)
    Contenido   = models.TextField(max_length=5000)
    imagen      = models.ImageField(upload_to="Home/Productos")
    Creado      = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = '02Producto'
        verbose_name_plural = '02Productos'
    
    def __str__(self):
        return self.Titulo

class a3Servicios(models.Model):
    Titulo      = models.CharField(max_length=50)
    Contenido   = models.TextField(max_length=5000)
    imagen      = models.ImageField(upload_to="Home/Servicios")
    Creado      = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = '03Servicio'
        verbose_name_plural = '03Servicios'
    
    def __str__(self):
        return self.Titulo

class a4Negocio(models.Model):
    Contenido   = models.TextField(max_length=5000)
    imagen      = models.ImageField(upload_to="Home/Negocios")

    class Meta:
        verbose_name        = '04Negocio'
        verbose_name_plural = '04Negocios'
    
    def __str__(self):
        return self.Contenido

class a5Sifras(models.Model):
    Titulo      = models.CharField(max_length=50)
    Contenido   = models.TextField(max_length=5000)
    numero   = models.IntegerField()

    class Meta:
        verbose_name        = '05Sifra'
        verbose_name_plural = '05Sifras'
    
    def __str__(self):
        return self.Titulo

class a6Noticias(models.Model):
    Titulo      = models.CharField(max_length=50)
    Contenido   = models.TextField(max_length=5000)
    imagen      = models.ImageField(upload_to="Home/Noticias")
    Creado      = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = '06Noticia'
        verbose_name_plural = '06Noticios'
    
    def __str__(self):
        return self.Titulo


class a7Alianzas(models.Model):
    imagen  = models.ImageField(upload_to="Home/Alianza")

    class Meta:
        verbose_name        = '07Alianza'
        verbose_name_plural = '07Alianzas'
    
    def __str__(self):
        return 'alianza '+ str(self.id)