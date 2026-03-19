from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos_list, name='productos_list'),
    path('crear/', views.crear_producto, name='crear_producto'),
]