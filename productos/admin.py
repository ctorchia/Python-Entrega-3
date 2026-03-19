from django.contrib import admin
from productos.models import Productos

@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("cod_producto", "descripcion", "precio","cantidad")
    list_display_links = ("cod_producto",)
    search_fields = ("descripcion",)
    ordering = ("cod_producto",)