from bootstrap_datepicker.widgets import DatePicker
from django import forms


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
    ('nube', 'LIIADT-01 Computo en la nube',),
    ('comInventsivo', 'LIIADT-02 Computo intensivo'),
    ('sisIntel', 'LIIADT-03 Sistemas inteligentes de automatización'),
    ('desTecnol', 'LIIADT-04 Desarrollo de tecnología e innovación',),
    ('ctrlAut', 'LIIADT-05 Control y automatización'),
    ('tecProd', 'LIIADT-06 Desarrollo e innovación en tecnologías de producción'),
    ('inBiotec', 'LIIADT-07 Desarrollo e innovación de productos biotecnologías y tecnológicos')
)

OPCIONES_Academia= (
    ('sistemas ','Ingeniería en Sistemas Computacionales'),
    ('industrial','Ingeniería Industrial'),
    ('alimentarias','Ingeniería en Industrias Alimentarias'),
    ('civil','Ingeniería Civil'),
    ('electronica','Ingeniería Electrónica'),
    ('electromecanica','Ingeniería Electromecánica'),
    ('bioquimica','Ingeniería Bioquímica'),
    ('gestion','Ingeniería en Gestión Empresarial'),
    ('macatronica','Ingeniería Mecatrónica'),
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


class PreRegistroForm(forms.Form):
    #fecha_presentacion= forms.DateField(label="Fecha de presentación", required=True, widget= forms.DateInput(attrs={'class': 'form-group col-md-3', 
     ##   'format': 'mm/dd/aaaa', 'autoclose': True,}))
    fecha_presentacion = forms.DateField(
        label= "*Fecha de presentación",
        widget=DatePicker(
            attrs={
                "format": "dd/mm/aaaa",
                "autoclose": True,
                'class': 'form-control'
            }
        )
    )
    convocatoriaCPR = forms.CharField(
        disabled= True,
        label= "Convocatoria CPR",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control'  
            }))
    tipoInvest = forms.MultipleChoiceField(
        label   = "*Tipo de Investigación",
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_INV,)
    tipoSector = forms.MultipleChoiceField(
        label   = "*Tipo de Sector",
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_SECTOR)

    especifique = forms.CharField(
        label="Especique",
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
        label= "*Línea de Investigación",
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
    fecha_inicio = forms.DateField(
        label= "Fecha Inicio",
        widget=DatePicker(
            options={
                "format": "dd/aa/aaaa",
                "autoclose": True,
                "class": "form-group"
            }
        )
    )
    fecha_fin = forms.DateField(
        label= "Fecha Fin",
        widget=DatePicker(
            options={
                "format": "dd/mm/aaaa",
                "autoclose": True,
                "class": "col-md-5 form-group",
                'class': 'form-group'
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
