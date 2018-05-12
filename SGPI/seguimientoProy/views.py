from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView, FormView, UpdateView, CreateView
from .forms import LoginForm, UserForm, RCarrera, NuevoPreregistro
from .models import Proyecto, Perfil, Carrera
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.template import RequestContext
from django.http import JsonResponse
from django.utils import timezone
import time
from datetime import datetime, timedelta
# Create your views here.


"""class Login(FormView):
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
	template_name= "Finalizar.html"""

"""class RegistraUsuarios(CreateView):
	model= User
	template_name= 'usuarios.html'
	form_class= RegistroUsuarios
	success_url= '/'"""


def Loguear(request):
	print(request.user)	
	if request.method== 'POST':
		activo = Perfil.objects.all()
		for j in activo:
			if j.username== request.POST['name_user']:
				if j.is_active== False:
					return render (request, 'index.html', {'anonimo':'Usuario inhabilitado'})
		form= LoginForm(request.POST or None)
		if form.is_valid():
			data= form.cleaned_data
			nombre_usuarios = data.get('name_user')
			contra_usuarios = data.get('password_user')
			acceso= authenticate(username=nombre_usuarios, password=contra_usuarios)				
			if acceso is not None: 
				login(request, acceso)
				tipoUsuario= Perfil.objects.all()
				for i in tipoUsuario:					
					if i.username== nombre_usuarios:
						if i.tipo_usuario == "Docente Responsable":
							return redirect ('seguimientoProy:Docente')
						if i.tipo_usuario == "Oficina de Seguimiento de Proyectos de Investigación":
							return redirect ('seguimientoProy:Gestion')
						if i.tipo_usuario == "Subdirección de Investigación y Posgrado":
							return redirect ('seguimientoProy:Investigacion')
						if i.tipo_usuario == "Consejo de Investigación":
							return redirect ('seguimientoProy:Consejo')

			else:		
				return render(request, 'index.html', {'error':'Usuario o contraseña incorrectos'})
		
	else:
		form= LoginForm()

	return render(request, 'index.html', {'form':form})

def pruebaRU(request):	
	print(request.user)
	f2= UserForm(request.POST or None)		
	doce= Perfil.objects.all()

	if request.method == 'POST':

		if f2.is_valid():	
			f2.save()
			return render(request, 'usuarios.html', {'exitoso':'Se guardó'}) 	
	

	else:
		f2= UserForm()

	if 'btnB' in request.POST:
		doc= Perfil.objects.filter(last_name__startswith=request.POST.get('nDocente', 'Guest (or whatever)'))		
		contexto = {'docente':doc}
		if doc:
			return render (request, 'usuarios.html', contexto)
		else:
			return redirect('seguimientoProy:RegistroU')
			print (request.POST.get('seleccion', 'Guest (or whatever)'))

	for k in doce:
		while k.username in request.POST and 'baja' in request.POST:
			print(k.username)
			if k.username == 'Korina123' or k.username == 'Salome123':
				return render (request, 'usuarios.html', {'administrador': 'no se puede', 'docentes':doce})
			else:
				print("Dar de baja a", k.first_name)
				k.is_active= False
				k.save()
				return render(request, 'usuarios.html', {'baja': 'Adiós mocoso', 'docentes':doce})

		while k.username in request.POST and 'habilitar' in request.POST:
			print("Habilitar a", k.first_name)
			k.is_active= True
			k.save()
			return render(request, 'usuarios.html', {'activo': 'Hola mocoso', 'docentes':doce})	
		


	contexto = {'f2': f2, 'docentes': doce}
		

	return render(request, 'usuarios.html', contexto)

def Docente(request):
	usu = Perfil.objects.filter(username=request.user)
	if 'logout' in request.POST:
		logout(request)
		return redirect(Loguear)
	for r in usu:		
		if r.tipo_usuario == "Docente Responsable": 
			return render(request, 'baseDocente.html')
		if r.tipo_usuario=="Oficina de Seguimiento de Proyectos de Investigación":
			return redirect('seguimientoProy:Gestion')
		if r.tipo_usuario == "Subdirección de Investigación y Posgrado":
			return redirect('seguimientoProy:Investigacion')
		if r.tipo_usuario == "Consejo de Investigación":
			return redirect('seguimientoProy:Consejo')

	return render(request, 'baseDocente.html')

def Gestion(request):
	usu = Perfil.objects.filter(username=request.user)
	if 'logout' in request.POST:
		logout(request)
		return redirect(Loguear)
	for r in usu:		
		if r.tipo_usuario == "Oficina de Seguimiento de Proyectos de Investigación": 
			return render(request, 'baseGestion.html')
		if r.tipo_usuario=="Docente Responsable":
			return redirect('seguimientoProy:Docente')
		if r.tipo_usuario == "Subdirección de Investigación y Posgrado":
			return redirect('seguimientoProy:Investigacion')
		if r.tipo_usuario == "Consejo de Investigación":
			return redirect('seguimientoProy:Consejo')
	return render(request, 'baseGestion.html')

def Investigacion(request):
	usu = Perfil.objects.filter(username=request.user)
	if 'logout' in request.POST:
		logout(request)
		return redirect(Loguear)
	for r in usu:		
		if r.tipo_usuario == "Subdirección de Investigación y Posgrado": 
			return render(request, 'baseInvest.html')			
		if r.tipo_usuario=="Docente Responsable":
			return redirect('seguimientoProy:Docente')
		if r.tipo_usuario == "Oficina de Seguimiento de Proyectos de Investigación":
			return redirect('seguimientoProy:Gestion')
		if r.tipo_usuario == "Consejo de Investigación":
			return redirect('seguimientoProy:Consejo')
	return render(request, 'baseInvest.html')

def Consejo(request):
	usu = Perfil.objects.filter(username=request.user)
	if 'logout' in request.POST:
		logout(request)
		return redirect(Loguear)
	for r in usu:		
		if r.tipo_usuario == "Consejo de Investigacióno": 
			return render(request, 'baseComite.html')			
		if r.tipo_usuario=="Docente Responsable":
			return redirect('seguimientoProy:Docente')
		if r.tipo_usuario == "Oficina de Seguimiento de Proyectos de Investigación":
			return redirect('seguimientoProy:Gestion')
		if r.tipo_usuario == "Subdirección de Investigación y Posgrado":
			return redirect('seguimientoProy:Investigacion')
	return render(request, 'baseComite.html')

def Preregistro(request):
	if 'logout' in request.POST:
		logout(request)
		return redirect(Loguear)
	form = NuevoPreregistro(request.POST)
	proyect = Proyecto.objects.all()
	fecha= time.strftime("%Y-%m-%d")
	if request.method == "POST":
		if form.is_valid():
			for i in proyecto:
				i.fecha_presentacion = request.POST['fecha_presentacion']
				i.convocatoris_CPR = request.POST['convocatoris_CPR']
				i.tipoInvestigacion = request.POST['tipoInvestigacion']
				i.tipoSector = request.POST['tipoSector']
				i.lineaInvestigacion= request.POST['lineaInvestigacion']
				i.nombre_proyecto = request.POST['nombre_proyecto']
				i.inicio = request.POST['inicio']
				i.fin = request.POST['fin']
				i.save()
	else:
		form = NuevoPreregistro()

	return render(request, "PreRegistroForm.html", {'fecha':fecha, 'form':form}) 
		


def Finalizar(request):
	return render(request, 'Finalizar.html')

def Imprimir(request):
	response['Content-Disposition'] = 'attachment; filename="Preregistro.pdf"'









