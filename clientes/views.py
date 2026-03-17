from django.shortcuts import render
from clientes.models import Clientes

def inicio(request):
    return render(request, "clientes/inicio.html")



def listar_clientes(request):
   
    clientes_query = Clientes.objects.all()    # [:20] 
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