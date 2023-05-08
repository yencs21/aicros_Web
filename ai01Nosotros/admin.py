from django.contrib import admin
from . import models
# Register your models here. 
admin.site.register(models.Valores    )
admin.site.register(models.Historia   )
admin.site.register(models.Cronologia )
admin.site.register(models.Equipo     )
admin.site.register(models.ValoresFinal)