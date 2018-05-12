from django import forms
from django.contrib.auth.models import User
from .models import Proyecto, Carrera, Perfil, EstadoProyecto
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    name_user= forms.CharField(max_length= 20, required= True, label="", 
        widget= (forms.TextInput(attrs={"placeholder":"Usuario", "class": "form-control"})))   
    password_user= forms.CharField(max_length= 20, required= True, label="", 
        widget= (forms.PasswordInput(attrs={"placeholder":"Contraseña", "class": "form-control"})))  

    

class UserForm(UserCreationForm):
    class Meta:
        model= Perfil
        fields= '__all__' 
        exclude= ['password']       
        widgets= {
            'carrera': forms.Select(attrs={'class':'form-control'})
        }

class RCarrera(forms.ModelForm):
    class Meta: 
        model= Carrera
        fields= '__all__'

class REstado(forms.ModelForm):
    class Meta: 
        model= EstadoProyecto
        fields= '__all__'

class NuevoPreregistro(forms.ModelForm):
    class Meta:
        model= Proyecto
        fields = '__all__'
        widgets= {
            'folio_proyecto': forms.TextInput(attrs= {
                    "readonly":"readonly", 
                    'class': 'hidden',
                    'id': 'foliop'
                }),


            'convocatoris_CPR': forms.TextInput(attrs= {
                    "readonly":"readonly",
                    'class': 'form-control',
                    'id':'cpr'
                    #'value': '123QWE'
                }), 
            'nombre_proyecto': forms.Textarea(attrs= {
                'type': 'text',
                'rows': '5',
                'cols': '200',
                'class': 'form-control', 
                'id': 'id_nombreP',             
                }),
            'otro_sector':forms.TextInput(attrs= {
                'id': 'id_especifique',
                'disabled': 'true',
                'class': 'form-control'                
                })
        }






        

   