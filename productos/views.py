from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductoForm

def productos_list(request):
    productos = Productos.objects.all()
    return render(request, "productos/productos_list.html", {"productos": productos})

def ver_producto(request, cod_producto):
    try:
        producto = Productos.objects.get(cod_producto=cod_producto)
    except Productos.DoesNotExist:
        return render(request, "error_404.html")
    context = {
        "producto" : producto
    }
    return render(request, "productos/ver_productos.html",context)
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos_list")
    else:
        form = ProductoForm()

    return render(request, "productos/producto_form.html", {"form": form})