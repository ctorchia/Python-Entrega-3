from django.contrib import admin
from clientes.models import Clientes
# Register your models here.

# admin.site.register(Clientes)
@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "nro_cliente", "dni")
    list_display_links = ("nombre",)
    search_fields = ("dni",)
    list_filter = ("fecha_de_nacimiento",)
    ordering = ("nro_cliente", "nombre")
    readonly_fields = ("nro_cliente",)