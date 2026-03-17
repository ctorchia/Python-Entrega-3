from django.shortcuts import render, redirect
from clientes.models import Clientes
from clientes.forms import ClienteForm

def inicio(request):
    return render(request, "clientes/inicio.html")

def listar_clientes(request):
    nombre = request.GET.get("nombre")
    clientes_query = Clientes.objects.all()    # [:10] 
    if nombre is not None:
        clientes_query = Clientes.objects.filter(
            nombre__icontains=nombre
        )
    context = {
        "clientes_list": clientes_query
    }
    return render(request, "clientes/clientes_list.html", context)

def ver_cliente(request, nro_cliente):
    try:
        cliente = Clientes.objects.get(nro_cliente=nro_cliente)
    except Clientes.DoesNotExist:
        return render(request, "error_404.html")
    context = {
        "cliente" : cliente
    }
    return render(request, "clientes/ver_cliente.html",context)

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm()
    
    return render(request, "clientes/crear_cliente.html", {
        "form": form
    })