from django.urls import path
from . import views

urlpatterns = [
    path('proveedor', views.proveedores_list, name='proveedores_list'),
    path('crear/', views.crear_proveedor, name='crear_proveedor'),
]