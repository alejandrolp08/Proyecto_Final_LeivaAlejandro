from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from . import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()


# Create your views here.
def home(request):
    return render(request, "CORE/index.html")


#! LOGIN

def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "CORE/index.html", {"mensaje": "Inició sesión correctamente"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, "CORE/login.html", {"form": form})

#! REGISTRO


#@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "CORE/index.html", {"mensaje": "Usuario creado!"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "CORE/register.html", {"form": form})



#! EDITAR PERFIL

@login_required
def editProfile(request):
    
    #Instancia del login
    usuario = request.user
    
    #Si es metodo POST se ahc elo mismo que el agregar
    if request.method == "POST":
        miFormulario = forms.UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid(): #Si se pasa la validacion de Django
            miFormulario.save()
            messages.success(request, "User information updated successfully.")
            return redirect("CORE:home")
            #te manda al inicio de la pagina web
    
    #En caso no sea POST
    else:
        #Creo el formulario con los datos que voy a modificar
        miFormulario = forms.UserEditForm(instance=usuario)
        
    #Voy al html que me permite editar
    return render (request, "CORE/editprofile.html", {"miFormulario":miFormulario, "usuario": usuario})
