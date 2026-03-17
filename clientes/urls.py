from django.urls import path
from clientes.views import *

urlpatterns = [
    path("",inicio, name="inicio"),
    path("clientes_list/", listar_clientes, name="clientes_list"),
    path("ver_cliente/<int:nro_cliente>/", ver_cliente, name="ver_cliente"),
]