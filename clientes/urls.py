from django.urls import path
from clientes.views import *

urlpatterns = [
    path("",inicio, name="inicio")
]