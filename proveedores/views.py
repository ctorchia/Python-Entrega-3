from django.shortcuts import render
from django.urls import reverse_lazy
from proveedores.models import Proveedores
from django.views.generic import(
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView
)

class ProveedoresListView(ListView):
    model = Proveedores
    template_name = "proveedores/proveedores_list.html"
    context_object_name = "proveedores_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        nombre = self.request.GET.get("nombre")
        if nombre not in ["", None, " "]:
            return queryset.filter(nombre__icontains=nombre).order_by("-nombre")
        return queryset
    

class ProveedoresDetailView(DetailView):
    model = Proveedores
    template_name = "proveedores/ver_proveedor.html"
    context_object_name = "proveedor"
    slug_field = "nro_proveedor"
    slug_url_kwarg = "nro_proveedor"
    

class ProveedoresDeleteView(DeleteView):
    model = Proveedores
    slug_field = "nro_proveedor"
    slug_url_kwarg = "nro_proveedor"
    template_name = "proveedores/proveedores_confirm_delete.html"
    success_url = reverse_lazy("proveedores_list")


class ProveedoresUpdateView(UpdateView):
    model = Proveedores
    fields = ["nombre", "cuit"]
    slug_field = "nro_proveedor"
    slug_url_kwarg = "nro_proveedor"
    success_url = reverse_lazy("proveedores_list")


class ProveedoresCreateView(CreateView):
    model = Proveedores
    template_name = "proveedores/crear_proveedor.html"
    fields = ["nro_proveedor", "nombre", "cuit", "email"]
    success_url = reverse_lazy("proveedores_list")
