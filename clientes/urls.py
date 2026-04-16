from django.urls import path
from clientes.views import *

urlpatterns = [
    path("",inicio, name="inicio"),
    path("crear_cliente/", crear_cliente, name="crear_cliente"),
    path("ver_cliente/<int:nro_cliente>/", ver_cliente, name="ver_cliente"),
    path("clientes_list/", listar_clientes, name="clientes_list"),
    path("actualizar_cliente/<int:nro_cliente>/", actualizar_cliente, name="actualizar_cliente"),
    path("cliente/eliminar/<str:nro_cliente>/", eliminar_cliente, name="eliminar_cliente"),
]