from django.urls import path

from .views import PostProyecto, Docente, Gestion, Consejo, Investigacion

app_name = 'seguimientoProy'
urlpatterns = [
    path(
        'postProyecto/', PostProyecto.as_view(), name='publicarProyecto'),
    path(
        'Docente/', Docente.as_view(), name='publicarProyecto'),
    path(
        'Gestion/', Gestion.as_view(), name='publicarProyecto'),
    path(
        'Investigacion/', Investigacion.as_view(), name='publicarProyecto'),
  	path(
        'Consejo/', Consejo.as_view(), name='publicarProyecto'),

  
]


