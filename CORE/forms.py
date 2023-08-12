from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Quita los mensajes de ayuda
        # help_texts = {k: "" for k in fields}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class UserEditForm(UserCreationForm):
    
    #Aca de sefinen las opciones que quiere modiciar el usuario,
    #Se colocan las basicas, o normales
    username = forms.CharField(label= "Nombre de usuario",)
    email = forms.EmailField(label = "Modificar E-mail")
    first_name = forms.CharField(label = "Nombre", required=False)
    last_name = forms.CharField(label = "Apellido", required=False)
    password1 = forms.CharField(label = "Contraseña", widget=forms.TextInput(attrs={'type': 'text'}))
    password2 = forms.CharField(label= "Repetir la contraseña", widget = forms.TextInput(attrs={'type': 'text'}))
    
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Esto pre rellenara el formulario con los campos de informacion ya existentes
        self.fields['username'].initial = self.instance.username
        self.fields['email'].initial = self.instance.email
        self.fields['password1'].initial = self.instance.password
        self.fields['password2'].initial = self.instance.password
        self.fields['first_name'].initial = self.instance.first_name
        self.fields['last_name'].initial = self.instance.last_name
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Update the user information with the modified data
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user