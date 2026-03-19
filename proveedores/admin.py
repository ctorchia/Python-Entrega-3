from django.contrib import admin
from proveedores.models import Proveedores

@admin.register(Proveedores)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nro_proveedor", "cuit")
    list_display_links = ("nombre",)
    search_fields = ("cuit",)
    ordering = ("nro_proveedor", "nombre")
    readonly_fields = ("nro_proveedor",)
