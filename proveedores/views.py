from django.shortcuts import render, redirect
from .models import Proveedores
from .forms import ProveedorForm
def proveedores_list(request):
    proveedores_list = Proveedores.objects.all()
    return render(request, "proveedores/proveedores_list.html", {"proveedores_list": proveedores_list})



def listar_proveedores(request):
    nombre = request.GET.get("nombre")
    proveedores_query = Proveedores.objects.all() 
    if nombre is not None:
        proveedores_query = Proveedores.objects.filter(
            nombre__icontains=nombre
        )
    context = {
        "proveedores_list": proveedores_query
    }
    return render(request, "proveedores/proveedores_list.html", context)



def ver_proveedor(request, nro_proveedor):
    try:
        proveedor = Proveedores.objects.get(nro_proveedor=nro_proveedor)
    except Proveedores.DoesNotExist:
        return render(request, "error_404.html")
    context = {
        "proveedor" : proveedor
    }
    return render(request, "proveedores/ver_proveedor.html",context)


def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proveedores_list")
    else:
        form = ProveedorForm()

    return render(request, "proveedores/crear_proveedor.html", {"form": form})