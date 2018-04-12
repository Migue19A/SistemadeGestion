from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, UpdateView, CreateView
from .forms import PreRegistroForm, LoginForm, RegistroUsuarios
from .models import Proyecto
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.


class Login(FormView):
    template_name = 'index.html'
    form_class= LoginForm


class Docente(TemplateView):
    template_name = 'baseDocente.html'


class Gestion(TemplateView):
    template_name = 'baseGestion.html'


class Consejo(TemplateView):
    template_name = 'baseComite.html'


class Investigacion(TemplateView):
    template_name = 'baseInvest.html'


class PreRegistro(FormView):
    template_name = 'PreRegistroForm.html'
    form_class = PreRegistroForm

class Finalizar(TemplateView):
	template_name= "Finalizar.html"

class RegistraUsuarios(CreateView):
	model= User
	template_name= 'usuarios.html'
	form_class= RegistroUsuarios
	success_url= reverse


def Loguear(request):
	if request.method== 'POST':
		form= LoginForm(request.POST or None)
		if form.is_valid():
			data= form.cleaned_data
			nombre_usuarios = data.get("name_user")
			contra_usuarios = data.get("password_user")
			acceso= authenticate(username=nombre_usuarios, password=contra_usuarios)
			if acceso is not None:
				print("Bienvenido")
				login(request, acceso)
				if nombre_usuarios== "Docente":
					return redirect ('seguimientoProy:Docente')
				if nombre_usuarios== "Gestión":
					return redirect ('seguimientoProy:Gestion')
				if nombre_usuarios== "Investigación":
					return redirect ('seguimientoProy:Gestion')
				if nombre_usuarios== "Consejo":
					return redirect ('seguimientoProy:Gestion')

			else:		
				print("No eres bienvenido")
		
	else:
		form= LoginForm()

	return render(request, 'index.html', {'form':form})





