from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Documentos)
admin.site.register(models.Contratos)
admin.site.register(models.Servicios)
admin.site.register(models.Catalogos)
admin.site.register(models.Otros    )