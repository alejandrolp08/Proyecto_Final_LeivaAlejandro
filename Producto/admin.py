from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Productos"


@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "categoria",
        "nombre",
        "precio",
        "cantidad",
        "descripcion",
        "fecha_actualizacion"
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = (
        "categoria",
        "nombre"
    )
    list_filter = ("categoria",)
    date_hierarchy = "fecha_actualizacion"

admin.site.register(models.Avatar)
