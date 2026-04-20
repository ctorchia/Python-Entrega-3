from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos
from .forms import ProductoForm, ProductoUpdateForm

def productos_list(request):
    productos_list = Productos.objects.all()
    return render(request, "productos/productos_list.html", {"productos_list": productos_list})


def listar_productos(request):
    descripcion = request.GET.get("descripcion")
    productos_query = Productos.objects.all()    # [:10] 
    if descripcion is not None:
        productos_query = Productos.objects.filter(
            descripcion__icontains=descripcion
        )
    context = {
        "productos_list": productos_query
    }
    return render(request, "productos/productos_list.html", context)


def ver_producto(request, cod_producto):
    try:
        producto = Productos.objects.get(cod_producto=cod_producto)
    except Productos.DoesNotExist:
        return render(request, "error_404.html")
    context = {
        "producto" : producto
    }
    return render(request, "productos/ver_producto.html",context)

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos_list")
    else:
        form = ProductoForm()

    return render(request, "productos/crear_producto.html", {"form": form})

def actualizar_producto(request, cod_producto):
    producto = get_object_or_404(Productos, cod_producto=cod_producto)
    if request.method == "POST":
        form = ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("productos_list")
    else:
        form = ProductoUpdateForm(instance=producto)

    context = {"form": form}
    return render(request, "clientes/actualizar_cliente.html", context)


def eliminar_producto(request, cod_producto):
    producto = get_object_or_404(Productos, cod_producto=cod_producto)
    if request.method == "POST":
        producto.delete()
        return redirect("productos_list")
    return redirect("productos_list")