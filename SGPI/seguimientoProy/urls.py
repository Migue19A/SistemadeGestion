from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import Docente, Gestion, Consejo, Investigacion, PreRegistro, Finalizar, pruebaRU
app_name = 'seguimientoProy'
urlpatterns = [
    path('Docente/', login_required(Docente), name='Docente'),
    path('Gestion/', login_required(Gestion), name='Gestion'),
    path('Investigacion/', login_required(Investigacion), name='Investigacion'),
    path('Consejo/', login_required(Consejo), name='Consejo'),
    path('Docente/PreRegistro/', login_required(PreRegistro.as_view()), name='preRegistro'),
    path('Docente/PreRegistro/Finalizar.html', login_required(Finalizar.as_view()), name='Finalizar'),
    path('Gestion/GestiondeUsuarios', login_required(pruebaRU), name='RegistroU')
]