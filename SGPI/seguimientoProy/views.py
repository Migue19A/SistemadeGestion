from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .forms import PreRegistroForm
from .models import Proyecto

# Create your views here.


class PostProyecto(TemplateView):
    template_name = 'base.html'


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
