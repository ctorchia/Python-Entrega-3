from django.urls import path
from proveedores.views import *

urlpatterns = [
    path("", ProveedoresListView.as_view(), name="proveedores_list"),
    path("crear_proveedor/", ProveedoresCreateView.as_view(), name="crear_proveedor"),
    path("<int:nro_proveedor>/actualizar/", ProveedoresUpdateView.as_view(), name="actualizar_proveedor"),
    path("<int:nro_proveedor>/eliminar/", ProveedoresDeleteView.as_view(), name="eliminar_proveedor"),
    path("<int:nro_proveedor>/ver/", ProveedoresDetailView.as_view(), name="ver_proveedor"),
]