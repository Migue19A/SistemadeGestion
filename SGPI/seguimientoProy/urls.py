from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import Docente, Gestion, Consejo, Investigacion, Finalizar, pruebaRU, Imprimir
app_name = 'seguimientoProy'
urlpatterns = [
    path('Docente/', login_required(Docente), name='Docente'),
    path('Gestion/', login_required(Gestion), name='Gestion'),
    path('Investigacion/', login_required(Investigacion), name='Investigacion'),
    path('Consejo/', login_required(Consejo), name='Consejo'),
    #path('Docente/PreRegistro/', login_required(PreRegistro), name='preRegistro'),
    path('Docente/PreRegistro/Finalizar', login_required(Finalizar), name='Finalizar'),
    path('Docente/PreRegistro/Finalizar/Imprimir', login_required(Imprimir), name='Imprimir'),
    path('GestiondeUsuarios', login_required(pruebaRU), name='RegistroU')
]