from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm
def proveedores_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, "proveedores/proveedores_list.html", {"proveedores": proveedores})

def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proveedores_list")
    else:
        form = ProveedorForm()

    return render(request, "proveedores/proveedor_form.html", {"form": form})