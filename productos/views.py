from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductoForm

def productos_list(request):
    productos = Productos.objects.all()
    return render(request, "productos/productos_list.html", {"productos": productos})


def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos_list")
    else:
        form = ProductoForm()

    return render(request, "productos/producto_form.html", {"form": form})