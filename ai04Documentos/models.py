from django.db import models
 
# Create your models here. 
class Documentos(models.Model):
    Titulo  = models.CharField( max_length = 500 )
    Doc     = models.FileField(null=True,blank=True)#upload_to="",

    class Meta:
        verbose_name        = '01Documento'
        verbose_name_plural = '01Documentos'
    
    def __str__(self):
        return self.Titulo

class Contratos(models.Model):
    Titulo  = models.CharField( max_length = 500 )
    Doc     = models.FileField(null=True,blank=True)

    class Meta:
        verbose_name        = '02Contrato'
        verbose_name_plural = '02Contratos'
    
    def __str__(self):
        return self.Titulo

class Servicios(models.Model):
    Titulo  = models.CharField( max_length = 500 )
    Doc     = models.FileField(null=True,blank=True)

    class Meta:
        verbose_name        = '03Servicio'
        verbose_name_plural = '03Servicios'
    
    def __str__(self):
        return self.Titulo

class Catalogos(models.Model):
    Titulo  = models.CharField( max_length = 500 )
    Doc     = models.FileField(null=True,blank=True)
    
    class Meta:
        verbose_name        = '04Catalogo'
        verbose_name_plural = '04Catalogos'
    
    def __str__(self):
        return self.Titulo

class Otros(models.Model):
    Titulo  = models.CharField( max_length = 500 )
    Doc     = models.FileField(null=True,blank=True)

    class Meta:
        verbose_name        = '05Otro'
        verbose_name_plural = '05Otros'
    
    def __str__(self):
        return self.Titulo