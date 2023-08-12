from django import forms

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Usuarios
        fields = ["nombre", "apellido", "email", "edad", "pais"]
