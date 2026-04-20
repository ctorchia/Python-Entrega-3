from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.productos_list, name='productos_list'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path("ver_producto/<int:cod_producto>/", views.ver_producto, name="ver_producto"),
    path("productos_list/", views.listar_productos, name="productos_list"),
    path("actualizar_producto/<int:cod_producto>/", views.actualizar_producto, name="actualizar_producto"),
    path("productos/eliminar/<str:cod_producto>/", views.eliminar_producto, name="eliminar_producto"),
]