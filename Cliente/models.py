from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return f" Nombre: {self.nombre} {self.apellido} - {self.pais}"
