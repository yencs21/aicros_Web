from django.contrib import admin
from .models import a1Promociones,a2Productos,a3Servicios,a4Negocio,a5Sifras,a6Noticias,a7Alianzas

# Register your models here.
class PromocionesAdmin(admin.ModelAdmin):
    readonly_fields = ('Creado','Actualizado')

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('Creado','Actualizado')

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ('Creado','Actualizado')

admin.site.register(a1Promociones ,   PromocionesAdmin)
admin.site.register(a2Productos   ,   PromocionesAdmin)
admin.site.register(a3Servicios   ,   ServiciosAdmin)
admin.site.register(a4Negocio     )
admin.site.register(a5Sifras      )
admin.site.register(a6Noticias    )
admin.site.register(a7Alianzas    )
