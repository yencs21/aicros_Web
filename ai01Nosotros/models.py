from django.db import models

# Create your models here.  
class Valores(models.Model):
    Titulo      = models.CharField(max_length=50)
    Contenido   = models.TextField(max_length=5000)

    class Meta:
        verbose_name        = '01Valore'
        verbose_name_plural = '01Valores'
    def __str__(self):
        return self.Titulo
    
class Historia(models.Model):
    Periodo     = models.CharField(max_length=15)
    
    class Meta:
        verbose_name        = '02Historia_Periodo'
        verbose_name_plural = '02Historias_Periodos'
    
    def __str__(self):
        return self.Periodo

class Cronologia(models.Model):
    Agno        = models.IntegerField()
    Contenido   = models.TextField(max_length=100)
    Periodo     = models.ForeignKey(Historia,on_delete=models.CASCADE)#Cuando el usuario se elimine se elimine todos los post que este creo

    class Meta:
        verbose_name        = '02Historia'
        verbose_name_plural = '02Historias'

    def __str__(self):
        return str(self.Agno)
    

class Equipo(models.Model):
    Nombre      = models.CharField(max_length=50)
    Apellido    = models.CharField(max_length=50)
    Cargo       = models.CharField(max_length=50)
    FotoPerfil  = models.ImageField()

    class Meta:
        verbose_name        = '03Equipo'
        verbose_name_plural = '03Equipos'

    def __str__(self):
        return self.Nombre

class ValoresFinal(models.Model):
    Titulo      = models.CharField(max_length=50)
    Contenido   = models.TextField(max_length=5000)

    class Meta:
        verbose_name        = '04Valore_Final'
        verbose_name_plural = '04Valores_Finales'
    def __str__(self):
        return self.Titulo