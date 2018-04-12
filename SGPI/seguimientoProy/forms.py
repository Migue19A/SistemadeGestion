from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

OPCIONES_INV = (
    ('aplicada', 'Investigación Aplicada',),
    ('experimental', 'Investigación Experimental'),
    ('basica', 'Investigación Básica'),
)
OPCIONES_SECTOR = (
    ('publico', 'Público',),
    ('privado', 'Privado'),
    ('educativo', 'Educativo'),
    ('social', 'Social',),
    ('productivo', 'Productivo'),
)
OPCIONES_LineaInvest = (
    ('nube', 'LIIADT-01 Cómputo en la nube',),
    ('comInventsivo', 'LIIADT-02 Cómputo intensivo'),
    ('sisIntel', 'LIIADT-03 Sistemas inteligentes de automatización'),
    ('desTecnol', 'LIIADT-04 Desarrollo de tecnología e innovación',),
    ('ctrlAut', 'LIIADT-05 Control y automatización'),
    ('tecProd', 'LIIADT-06 Desarrollo e innovación en tecnologías de producción'),
    ('inBiotec', 'LIIADT-07 Desarrollo e innovación de productos biotecnologías y tecnológicos')
)

OPCIONES_Academia= (
    ('sistemas ','Ingeniería en sistemas computacionales'),
    ('industrial','Ingeniería industrial'),
    ('alimentarias','Ingeniería en industrias alimentarias'),
    ('civil','Ingeniería civil'),
    ('electronica','Ingeniería electrónica'),
    ('electromecanica','Ingeniería electromecánica'),
    ('bioquimica','Ingeniería bioquímica'),
    ('gestion','Ingeniería en gestión empresarial'),
    ('macatronica','Ingeniería mecatrónica'),
    ('gastronomia','Gastronimía'),
)

OPCIONES_Colaborador = (
    ('1', '1',),
    ('2', '2'),
    ('3', '3'),
    ('4', '4',),
)

OPCIONES_Docente = (
    ('nombre', 'Docente',),
)

OPCIONES_Convenio = (
    ('si', 'Sí',),
    ('no', 'No',),
)
OPCIONES_ProductosA= (
    ('servicio','Servicio Social'),    
    ('residencia','Residencia Profesional'),
    ('tesis','Tesis'),
    ('ponencias','Ponencias/Conferencias'),
    ('articulos','Artículos'),
    ('libros','Libros/Manuales')
)

OPCIONES_Financi = (
    ('interno', 'Interno',),
    ('externo', 'Externo',),
)

OPCIONES_Alumno = (
    ('servs', 'Servicio Social',),
    ('resip', 'Residencia Profesional',),
    ('tesis', 'Tesis',),
)

OPCIONES_Semestre = (
    ('1', '1°',),
    ('2', '2°',),
    ('3', '3°',),
    ('4', '4°',),
    ('5', '5°',),
    ('6', '6°',),
    ('7', '7°',),
    ('8', '8°',),
    ('9', '9°',),
    ('10', '10°',),
    ('11', '11°',),
    ('12', '12°',),
    ('13', '13°',),

)

OPCIONES_Carrera= (
    ('sistemas ','Ingeniería en sistemas computacionales'),
    ('industrial','Ingeniería industrial'),
    ('alimentarias','Ingeniería en industrias alimentarias'),
    ('civil','Ingeniería civil'),
    ('electronica','Ingeniería electrónica'),
    ('electromecanica','Ingeniería electromecánica'),
    ('bioquimica','Ingeniería bioquímica'),
    ('gestion','Ingeniería en gestión empresarial'),
    ('macatronica','Ingeniería mecatrónica'),
    ('gastronomia','Gastronimía'),
)

class PreRegistroForm(forms.Form):
    
    fecha_presentacion = forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    convocatoriaCPR = forms.CharField(
        disabled= True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))
    tipoInvest = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_INV,)
    tipoSector = forms.MultipleChoiceField(
        label   = "*Tipo de Sector",
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_SECTOR)

    especifique = forms.CharField(
        max_length=256,
        disabled= True,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '5',
                'cols': '200',
                'class': 'form-control'

            }))
    lineaInv = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_LineaInvest)
    
    nombreProy = forms.CharField(
        label= "*Nombre del Proyecto (Máximo 200 caracteres)",
        required= True,
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control'

            }))

    fecha_inicio= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    fecha_fin= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )


    nombreDoc = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }))
    apPat = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }))
    apMat = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }))

    estudiosMax = forms.CharField(
        max_length= 50,
        required= True,
        label= "Grado máximo de estudios", 
        widget= forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
            )
        )

    academia= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control'}),
        choices= OPCIONES_Academia)

    personal= forms.CharField(
        required= True,
        max_length=5000000,
        widget=forms.TextInput(
            attrs={
                'type': 'number', 
                'class': 'form-control'  
    }))

    movil = forms.CharField(
        widget= forms.TextInput(
            attrs= { 
                'type': 'number',                
                'class': 'form-control',                 
                'pattern':'^\d{10}$' 
            }
            )

        )

    correoI = forms.EmailField(
        required= True,
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control'})
        )

    correoA = forms.EmailField(
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control'})
        )


    actividades = forms.CharField(
        required= True,
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control'

            }))


    palabrasClave = forms.CharField(
        required= True,
        max_length=50,
        widget= forms.TextInput(
            attrs= { 
                'type': 'text',   
                'onKeyPress': 'return palabrasClave(event)',             
                'class': 'form-control' 
            }
            )

        )

    ncolaborador= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control', 'id': 'opcion_colabora', 'onchange':'muestra_colaborador()'}),
        choices= OPCIONES_Colaborador)


    sDocente= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control'}),
        choices= OPCIONES_Docente)


    nombreDoc2 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'nombresCol2'
            }))
    apPat2 = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'apCol2'
            }))
    apMat2 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'amCol2'
            }))

    estudiosMax2 = forms.CharField(
        max_length= 50,
        required= True,
        label= "Grado máximo de estudios", 
        widget= forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'gradoMCol2'
            }
            )
        )

    academia2= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control', 'id': 'programaCol2'}),
        choices= OPCIONES_Academia)

    personal2= forms.CharField(
        required= True,
        max_length=5000000,
        widget=forms.TextInput(
            attrs={
                'type': 'number', 
                'class': 'form-control',
                'id': 'noPersonalCol2'  
    }))

    movil2 = forms.CharField(
        max_length=100000000,
        widget= forms.TextInput(
            attrs= { 
                'type': 'number',                
                'class': 'form-control',
                'id': 'movilCol2',                 
                'pattern':'^\d{10}$'  
            }
            )

        )

    correoI2 = forms.EmailField(
        required= True,
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control', 'id': 'correoCol2'})
        )

    correoA2 = forms.EmailField(
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control', 'id': 'correoAlCol2'})
        )


    actividades2 = forms.CharField(
        required= True,
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
                'id': 'actividadesCol2'
    }))

    nombreDoc3 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'nombresCol3'
            }))
    apPat3 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'apCol3'
            }))
    apMat3 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'amCol3'
            }))

    estudiosMax3 = forms.CharField(
        max_length= 50,
        required= True,
        label= "Grado máximo de estudios", 
        widget= forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'gradoMCol3'
            }
            )
        )

    academia3= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control', 'id': 'programaCol3'}),
        choices= OPCIONES_Academia)

    personal3= forms.CharField(
        required= True,
        max_length=5000000,
        widget=forms.TextInput(
            attrs={
                'type': 'number', 
                'class': 'form-control',
                'id': 'noPersonalCol3'  
    }))

    movil3 = forms.CharField(
        max_length=100000000,
        widget= forms.TextInput(
            attrs= { 
                'type': 'number',                
                'class': 'form-control',
                'id': 'movilCol3',                 
                'pattern':'^\d{10}$'  
            }
            )

        )

    correoI3 = forms.EmailField(
        required= True,
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control', 'id': 'correoCol3'})
        )

    correoA3 = forms.EmailField(
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control', 'id': 'correoAlCol3'})
        )


    actividades3 = forms.CharField(
        required= True,
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
                'id': 'actividadesCol3'
    }))

    nombreDoc4 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'nombresCol4'
            }))
    apPat4 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'apCol4'
            }))
    apMat4 = forms.CharField(
        max_length=50,
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'amCol4'
            }))

    estudiosMax4 = forms.CharField(
        max_length= 50,
        required= True,
        label= "Grado máximo de estudios", 
        widget= forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'gradoMCol4'
            }
            )
        )

    academia4= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control', 'id': 'programaCol4'}),
        choices= OPCIONES_Academia)

    personal4= forms.CharField(
        required= True,
        max_length=5000000,
        widget=forms.TextInput(
            attrs={
                'type': 'number', 
                'class': 'form-control',
                'id': 'noPersonalCol4'  
    }))

    movil4 = forms.CharField(
        max_length=100000000,
        widget= forms.TextInput(
            attrs= { 
                'type': 'number',                
                'class': 'form-control',
                'id': 'movilCol4',                 
                'pattern':'^\d{10}$'  
            }
            )

        )

    correoI4 = forms.EmailField(
        required= True,
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control', 'id': 'correoCol4'})
        )

    correoA4 = forms.EmailField(
        max_length=500,
        widget= forms.TextInput (attrs= {'type': 'email', 'class': 'form-control', 'id': 'correoAlCol4'})
        )


    actividades4 = forms.CharField(
        required= True,
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
                'id': 'actividadesCol4'
    }))

    objetivoG = forms.CharField(
        required= True,
        max_length=512,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    objetivoE = forms.CharField(
        required= True,
        max_length=512,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    resultados = forms.CharField(
        required= True,
        max_length=512,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    convenio = forms.ChoiceField(
        required=True,
        widget= forms.RadioSelect(attrs={'onclick': 'vinculacionConvenio()'}),
        choices= OPCIONES_Convenio
    )

    aporta = forms.ChoiceField(
        required=True,
        widget= forms.RadioSelect(attrs={'onclick': 'respuestaF()'}),
        choices= OPCIONES_Convenio
    )

    nombre_organizacion = forms.CharField(
        required= True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))

    direccion_organizacion = forms.CharField(
        required= True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))

    area_organizacion = forms.CharField(
        required= True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))

    telefono_organizacion = forms.CharField(
        required= True,
        widget=forms.TextInput(
            attrs={
                'type': 'number', 
                'class': 'form-control',  
                'pattern':'^\d{10}$'
            }))

    nombreC_organizacion = forms.CharField(
        required= True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))

    descripcion_organizacion = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    describa_aportaciones = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    productosA = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_ProductosA,)

    intelectual = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))

    otros = forms.CharField(
        required= True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))


    sEtapa= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'id':'opcion_etapas', 'class': 'form-control', 'onchange':'muestra_etapas()'}),
        choices= OPCIONES_Colaborador)

    n_Etapa = forms.CharField(
        required= True,
        max_length=24,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',  
            }))

    etapaInicio= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaTermino= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaMeses= forms.CharField(
        disabled=True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control'
            }
        )
    )

    etapaDes = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaAct = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaPro = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    n_Etapa2 = forms.CharField(
        required= True,
        max_length=24,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',  
            }))

    etapaInicio2= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaTermino2= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaMeses2= forms.CharField(
        disabled=True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control'
            }
        )
    )

    etapaDes2 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaAct2 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaPro2 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    n_Etapa3 = forms.CharField(
        required= True,
        max_length=24,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',  
            }))

    etapaInicio3= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaTermino3= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaMeses3= forms.CharField(
        disabled=True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control'
            }
        )
    )

    etapaDes3 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaAct3 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaPro3 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    n_Etapa4 = forms.CharField(
        required= True,
        max_length=24,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',  
            }))

    etapaInicio4= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaTermino4= forms.CharField(
        required= True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    etapaMeses4= forms.CharField(
        disabled=True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control'
            }
        )
    )

    etapaDes4 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaAct4 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))

    etapaPro4 = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',
                'class': 'form-control',
    }))


    etapaMeses4= forms.CharField(
        disabled=True,
        max_length= 20,
        widget= forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        )
    )

    financi = forms.ChoiceField(
        required=True,
        widget= forms.RadioSelect(attrs={'onclick': 'muestraFina()'}),
        choices= OPCIONES_Convenio
    )

    finanSi = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_Financi,)

    fEspeci= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                }   

            )

        )

    fInfra= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'infraestructura',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fCon= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'consumibles',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fLic= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'licencias',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fVia= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'viaticos',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fPubli= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'publicaciones',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fEqui= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'equipo',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fPat= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'patentes',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fOtros= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'otros',
                    'onkeyup': 'sumar()'
                }   

            )

        )

    fDesglo= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control'
                }   

            )

        )

    fTot= forms.CharField(
        disabled= True,
        widget= forms.TextInput(
                attrs={
                    'aria-describedb': 'inputGroupSuccess2Status',
                    'type': 'number',
                    'class': 'form-control',
                    'id':'total'
                }   

            )

        )

    alumTot= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'form-control',
                    'id':'totalA',
                    'max':'20',
                    'min': '0',
                    'value': '1',
                    'onkeyup': 'ValidaMaximo()',  
                    'onkeypress': 'return validaN(event)'
                }   

            )

        )

    alumNomb= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control'
                }  
            )
        )


    alumSRT = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_Alumno,)

    alumControl= forms.CharField(
        widget= forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control'
                }  
            )
        )

    alumSem= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control'}),
        choices= OPCIONES_Semestre)

    alumCar= forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control'}),
        choices= OPCIONES_Carrera)

    alumActi = forms.CharField(
        required= True,
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '5',
                'cols': '200',
                'class': 'form-control'

            }))


class LoginForm(forms.Form):
    name_user= forms.CharField(max_length= 20, required= True, label="", 
        widget= (forms.TextInput(attrs={"placeholder":"Usuario", "class": "form-control"})))   
    password_user= forms.CharField(max_length= 20, required= True, label="", 
        widget= (forms.PasswordInput(attrs={"placeholder":"Contraseña", "class": "form-control"})))  


class RegistroUsuarios(UserCreationForm):
    class Meta:
        model= User
        fields= [
                'username',
                'first_name',
                'last_name',
                'email'
        ]

        labels= {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo'
        }
        

   