from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.proveedores_list, name='proveedores_list'),
    path('crear/', views.crear_proveedor, name='crear_proveedor'),
    path("ver_proveedor/<int:nro_proveedor>/", views.ver_proveedor, name="ver_proveedor"),
]