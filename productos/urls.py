from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.productos_list, name='productos_list'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path("ver_producto/<int:cod_producto>/", views.ver_producto, name="ver_producto"),
    path("productos_list/", views.listar_productos, name="productos_list"),
]