from django.urls import path

from . import views

app_name = "Cliente"

urlpatterns = [
    path('',views.home, name="home"),
    path('crear_clientes/', views.crear_clientes, name="crear_clientes"),
    path('crear/', views.crear_cliente, name="crear"),
    path('busqueda/', views.busqueda, name="busqueda")
]
