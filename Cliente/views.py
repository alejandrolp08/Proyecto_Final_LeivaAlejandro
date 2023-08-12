
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from . import forms

# Create your views here.

from .models import Usuarios, Pais

def home(request):
    clientes_registros = Usuarios.objects.all()
    contexto = {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "cliente/index.html", contexto)
    
def crear_clientes(request):


    p1 = Pais(nombre="Perú")
    p2 = Pais(nombre="Estados Unidos")
    p3 = Pais(nombre="Brasil")

    p1.save()
    p2.save()
    p3.save()

    c1 = Usuarios(nombre="Rosa", apellido="Pimentel", email = "rpimentel@hotmail.com", edad = "72", pais=p1)
    c2 = Usuarios(nombre="Ruben", apellido="Pimentel", email = "rubenpm@hotmail.com", edad = "68", pais=p1)
    c3 = Usuarios(nombre="Omar", apellido="Leiva", email = "omarleiva@hotmail.com", edad = "27", pais=p2)
    #c4 = Usuarios(nombre="Danielle", apellido="Alvarez", email = "daniellealvarez@hotmail.com", edad = "28", pais=None)

    c1.save()
    c2.save()
    c3.save()
    #c4.save()
    return redirect("Cliente:home")


def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:  # request.method == "GET"
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})


def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "Pimen"
    cliente_nombre = Usuarios.objects.filter(nombre__contains="Pimen")

    # País de origen vacío
    cliente_pais = Usuarios.objects.filter(pais=None)

    contexto = {
        "clientes_nombre": cliente_nombre,
        "clientes_pais": cliente_pais
    }
    return render(request, "cliente/search.html", contexto)