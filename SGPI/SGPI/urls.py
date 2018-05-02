"""SGPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from seguimientoProy.views import Loguear

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('Principal/', include('seguimientoProy.urls'), name='Principal'),
    url(r'^accounts/login/', Loguear, name='inicio'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^reset/password_reset', password_reset, {'template_name': 'reestablecer_form.html',
         'email_template_name': 'reestablecer_correo.html'}, name='password_reset'),
    url(r'^password_reset_done', password_reset_done, {'template_name':'reestablecer_enviada.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'reestablecer_completo.html'}, name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name':'reestablecer_final.html'}, name='password_reset_complete')
]
