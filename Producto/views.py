
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
#! importaciones para login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

# PAGINA PRINCIPAL


@login_required
def index(request):
    return render(request, "Producto/index.html")

# ***** PRODUCTOCATEGORIA

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("Producto:productocategoria_list")

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("Producto:productocategoria_list")

class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("Producto:productocategoria_list")


# ***** PRODUCTO

class ProductoList(ListView):
    model = models.Producto

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Producto:producto_list")

class ProductoDetail(DetailView):
    model = models.Producto

class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Producto:producto_list")

class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("Producto:producto_list")