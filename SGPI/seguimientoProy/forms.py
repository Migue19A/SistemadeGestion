from bootstrap_datepicker.widgets import DatePicker
from django import forms


OPCIONES_INV = (
    ('aplicada', 'Aplicada',),
    ('experimental', 'Experimental'),
    ('basica', 'Basica'),
)
OPCIONES_SECTOR = (
    ('publico', 'Público',),
    ('privado', 'Privado'),
    ('educativo', 'Educativo'),
    ('social', 'Social',),
    ('productivo', 'Productivo'),
    ('otro', 'Otro'),
)
OPCIONES_LineaInvest = (
    ('nube', 'LIIADT-01 Computo en la nube',),
    ('comInventsivo', 'LIIADT-02 Computo intensivo'),
    ('sisIntel', 'LIIADT-03 Sistemas inteligentes de automatización'),
    ('desTecnol', 'LIIADT-04 Desarrollo de tecnología e innovación',),
    ('ctrlAut', 'LIIADT-05 Control y automatización'),
    ('tecProd', 'LIIADT-06 Desarrollo e innovación en tecnologías de producción'),
    ('inBiotec', 'LIIADT-07 Desarrollo e innovación de productos biotecnologías y tecnológicos'),

)


class PreRegistroForm(forms.Form):

    fecha_presentacion = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )
    convocatoriaCPR = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }))
    tipoInvest = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_INV,)
    tipoSector = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_SECTOR,)
    especifique = forms.CharField(
        max_length=256,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '5',
                'cols': '200',

            }))
    lineaInv = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPCIONES_LineaInvest,)
    nombreProy = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'rows': '4',
                'cols': '200',

            }))
    fecha_inicio = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True,
                "class": " col-lg-5"
            }
        )
    )
    fecha_fin = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True,
                "class": " col-lg-5"
            }
        )
    )
    nombreDoc = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }))
    apPat = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }))
    apMat = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }))
