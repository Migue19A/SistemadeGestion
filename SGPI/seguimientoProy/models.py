from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class Proyecto(models.Model):
    folio_proyecto = models.CharField(primary_key=True, max_length=7)
    fecha_presentacion = models.DateTimeField('fecha presentacion')
    fecha_reactivacion = models.DateTimeField('fecha reactivacion')
    palabra_clave1 = models.CharField(max_length=45)
    palabra_clave2 = models.CharField(max_length=45)
    palabra_clave3 = models.CharField(max_length=45)
    actividades_responsable = models.CharField(max_length=256)
    convocatoris_CPR = models.CharField(max_length=45)
    inicio = models.DateTimeField('fecha inicio')
    fin = models.DateTimeField('fecha fin')
    nombre_proyecto = models.CharField(max_length=45)
    objetivo_general = models.CharField(max_length=45)
    objetivo_especifico = models.CharField(max_length=45)
    resultados = models.CharField(max_length=45)
    tipoInvestigacion = models.ForeignKey(
        TipoInvestigacion, on_delete=models.CASCADE)
    tipoSector = models.ForeignKey(TipoSector, on_delete=models.CASCADE)
    lineaInvestigacion = models.ForeignKey(
        LineaInvestigacion, on_delete=models.CASCADE)


class TipoInvestigacion(models.Model):
    id_tipo_investigacion = models.IntegerField(primary_key=True)
    descripcion_tipo_investigacion = models.CharField(max_length=45)


class TipoSector(models.Model):
    id_tipo_sector = models.IntegerField(primary_key=True)
    descripcion_sector = models.CharField(max_length=45)


class LineaInvestigacion(models.Model):
    id_linea_investigacion = models.IntegerField(primary_key=True)
    descripcion_linea = models.CharField(max_length=45)


class ProyectosCancelados(models.Model):
    motivo = models.CharField(max_length=45)
    folio_proyecto = models.OneToOneField(
        Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    fecha_cancelacion = models.DateField('fecha cancelacion')
    responsable_anterior = models.CharField(max_length=45)


class CatObserv(models.Model):
    id_observaciones = models.IntegerField(primary_key=True)
    descripcion_observacion = models.CharField(max_length=45)


class Observaciones(models.Model):
    observaciones_gestion = models.CharField(max_length=1000)
    observaciones_investigacion = models.CharField(max_length=1000)
    observaciones_comite = models.CharField(max_length=1000)
    folio_proyecto = models.ManyToManyField(Proyecto,
                                            blank=True,
                                            )
    id_observaciones = models.ForeignKey(
        CatObserv, on_delete=models.CASCADE, null=True, blank=True)


class Financiamiento(models.Model):
    folio_proyecto = models.OneToOneField(
        Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    financ = models.BooleanField()
    interno = models.BooleanField()
    externo = models.BooleanField()
    especificar = models.CharField(max_length=45)
    infraestructura = models.DecimalField(max_digits=7, decimal_places=2)
    consumibles = models.DecimalField(max_digits=7, decimal_places=2)
    licencias = models.DecimalField(max_digits=7, decimal_places=2)
    viaticos = models.DecimalField(max_digits=7, decimal_places=2)
    publicaciones = models.DecimalField(max_digits=7, decimal_places=2)
    equipo = models.DecimalField(max_digits=7, decimal_places=2)
    patentes = models.DecimalField(max_digits=7, decimal_places=2)
    otros = models.DecimalField(max_digits=7, decimal_places=2)
    especifique = models.CharField(max_length=45)


class Metas(models.Model):
    folio_proyecto = models.OneToOneField(
        Proyecto, null=False, blank=False, on_delete=models.CASCADE)
    servicio = models.BooleanField()
    residencia = models.BooleanField()
    tesis = models.BooleanField()
    ponencia = models.BooleanField()
    articulos = models.BooleanField()
    libros = models.BooleanField()
    propiedad_intelectual = models.CharField(max_length=255)
    otros = models.CharField(max_length=255)


class Vinculacion(models.Model):
    folio_proyecto = models.OneToOneField(
        Proyecto, null=False, blank=False, on_delete=models.CASCADE)
    nombre_organizacion = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    area = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    nombre_completo_organ = models.CharField(max_length=45)
    descripcion_organizacion = models.CharField(max_length=255)
    descripcion_aportaciones = models.CharField(max_length=255)


"""class Usuario(models.Model):
    numero_personal = models.IntegerField(
        primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    ## fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    correo_institucional = models.EmailField()
    numero_personal = models.OneToOneField(
        Usuario, null=False, blank=False, on_delete=models.CASCADE)
    # tipo_usuario = models.CharFIeld(max_length=80)"""


class Carrera(models.Model):
    id_carrera = models.IntegerField(primary_key=True)
    descripcion_carrera = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.descripcion_carrera)


class Perfil (User):
    numero_personal = models.IntegerField(null=False)
    sexo = models.CharField(max_length=1)
    tipo_usuario = models.CharField(max_length=80)
    grado_maximo_estudios = models.CharField(max_length=45)
    telefono_movil = models.IntegerField(null=True, blank=True)
    carrera = models.ForeignKey(
        Carrera,
        null=False,
        blank=True,
        on_delete=models.CASCADE)


class ColaboradorDocente(models.Model):
    folio_proyecto = models.ForeignKey(
        Proyecto, null=True, blank=True, on_delete=models.CASCADE)
    actividades_colaborador = models.CharField(max_length=512)
    numero_personal = models.ForeignKey(
        Perfil, null=True, blank=False, on_delete=models.CASCADE)


class EstadoProyecto(models.Model):
    id_estado_proyecto = models.IntegerField(
        primary_key=True)
    descripcion_estado_proy = models.CharField(max_length=45)


class CatSancion(models.Model):
    id_catalogo_sancion = models.IntegerField(
        primary_key=True)
    descripcion_catalogo_sancion = models.CharField(max_length=45)


class Notificaciones(models.Model):
    id_notificaciones = models.IntegerField(
        primary_key=True)
    receptor = models.ForeignKey(
        Perfil, null=False, blank=False, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=45)
    fecha_notificacion = models.DateField('fecha de notificacion')
    estado_notificacion = models.BooleanField()
    vista = models.DateField('fecha de vistas')


class Sanciones(models.Model):
    numero_personal = models.ForeignKey(
        Perfil, null=False, blank=False, on_delete=models.CASCADE)
    id_catalogo_sancion = models.ForeignKey(
        CatSancion, null=False, blank=False, on_delete=models.CASCADE)
    fecha_sancion = models.DateField('fecha de sancion')
    folio_proyecto = models.ForeignKey(Proyecto, null=False,
                                       blank=False, on_delete=models.CASCADE)


class Alumno(models.Model):
    numero_control = models.CharField(primary_key=True, max_length=9)
    semestre = models.IntegerField()
    nombre_alumno = models.CharField(max_length=45)
    apellido_paterno_alumno = models.CharField(max_length=45)
    apellido_materno_alumno = models.CharField(max_length=45)
    id_carrera = models.ForeignKey(
        Carrera, null=False, blank=False, on_delete=models.CASCADE)
    actividades_alumno = models.CharField(max_length=256)


class CatMetasAlumno(models.Model):
    id_cat_metas_alumno = models.IntegerField(primary_key=True)
    descricpion = models.CharField(max_length=10)


class MetasAlumnos(models.Model):
    id_metas_alumno = models.IntegerField(primary_key=True)
    descricpion_metas_alumno = models.CharField(max_length=256)
    numero_control = models.ForeignKey(
        Alumno, null=False, blank=False, on_delete=models.CASCADE)
    folio_proyecto = models.ForeignKey(Proyecto, null=False,
                                       blank=False, on_delete=models.CASCADE)
    catalogo_metas_alumno = models.ForeignKey(
        CatMetasAlumno, null=False, blank=False, on_delete=models.CASCADE)


class Recepcion(models.Model):
    id_solicitud = models.IntegerField(primary_key=True)
    fecha_recepcion = models.DateField('fecha de recepcion')
    nombre_recibio = models.CharField(max_length=45)
    folio_proyecto = models.ForeignKey(Proyecto, null=False,
                                       blank=False, on_delete=models.CASCADE)


class Prorroga(models.Model):
    id_prorroga = models.IntegerField(primary_key=True)
    motivo = models.CharField(max_length=45)
    tiempo = models.IntegerField()
    observaciones_inv_gest = models.CharField(max_length=512)
    observaciones_inv_pro = models.CharField(max_length=512)
    observaciones_inv_com = models.CharField(max_length=512)
    folio_proyecto = models.ForeignKey(Proyecto, null=False,
                                       blank=False, on_delete=models.CASCADE)


class Etapas(models.Model):
    id_etapa = models.CharField(primary_key=True, max_length=7)
    nombre_etapa = models.CharField(max_length=45)
    fecha_inicio_etapa = models.DateField('fecha inicio de etapa')
    fecha_fin_etapa = models.DateField('fecha fin de etapa')
    meses = models.IntegerField()
    descricpion_etapa = models.CharField(max_length=256)
    metas = models.CharField(max_length=256)
    actiidades_etapa = models.CharField(max_length=256)
    productos = models.CharField(max_length=256)


class Entregables(models.Model):
    id_entregable = models.IntegerField(primary_key=True)
    fecha_entregable = models.DateField('fecha de entregable')
    observaciones_entregable = models.CharField(max_length=45)
    folio_proyecto = models.ForeignKey(Proyecto, null=False,
                                       blank=False, on_delete=models.CASCADE)
    id_etapa = models.ForeignKey(
        Etapas, null=False, blank=False, on_delete=models.CASCADE)


class Constancias(models.Model):
    folio_constancia = models.CharField(primary_key=True, max_length=10)
    fecha_constancia = models.DateField('fecha de constancia')
    mensaje = models.CharField(max_length=45)
    tipo_constancia = models.CharField(max_length=45)
    folio_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,
                                       null=False, blank=False)
    id_etapa = models.ForeignKey(Etapas, null=False,
                                 blank=False, on_delete=models.CASCADE)


class LogrosConocimiento(models.Model):
    id_logros_conocimiento = models.IntegerField(primary_key=True)
    avances_conocimiento = models.CharField(max_length=45)
    desarrollo_tecnologico = models.CharField(max_length=45)
    infraestructura_tecnologica = models.CharField(max_length=45)
    id_entregable = models.ForeignKey(
        Entregables, null=False, blank=False, on_delete=models.CASCADE)


class LogrosPresentaciones(models.Model):
    id_logros_present = models.IntegerField(primary_key=True)
    titulo_ponencia = models.CharField(max_length=45)
    tipo_ponencia = models.CharField(max_length=45)
    nombre_evento = models.CharField(max_length=45)
    lugar = models.CharField(max_length=45)
    fecha_logros_pres = models.DateField('fecha logros presentaciones')
    id_entregable = models.ForeignKey(Entregables, null=True,
                                      blank=True, on_delete=models.CASCADE)


class LogrosRecursosHumanos(models.Model):
    id_logros_rec_hum = models.IntegerField(primary_key=True)
    nombre_trabajo = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    id_entregable = models.ForeignKey(Entregables, null=True,
                                      blank=True, on_delete=models.CASCADE)


class LogrosDivulgacion(models.Model):
    id_logros_div = models.IntegerField(primary_key=True)
    titulo_articulo = models.CharField(max_length=45)
    tipo_publicacion = models.CharField(max_length=45)
    nombre_publicacion = models.CharField(max_length=45)
    lugar = models.CharField(max_length=45)
    fecha_logros_divulg = models.DateField('fecha devulgacion articulo')
    id_entregable = models.ForeignKey(Entregables, null=True,
                                      blank=True, on_delete=models.CASCADE)


class Resultados(models.Model):
    id_resultados = models.IntegerField(primary_key=True)
    resultados = models.CharField(max_length=45)
    anexos = models.CharField(max_length=45)
    id_entregable = models.ForeignKey(Entregables, null=False,
                                      blank=False, on_delete=models.CASCADE)


class ObservacionesEntreg(models.Model):
    id_observaciones_entreg = models.IntegerField(primary_key=True)
    observaciones_entregable_ges = models.CharField(max_length=1000)
    observaciones_entregable_inv = models.CharField(max_length=1000)
    observaciones_entregable_com = models.CharField(max_length=1000)
    id_observaciones = models.ForeignKey(CatObserv, null=True,
                                         blank=True, on_delete=models.CASCADE)


class ResumenEjecutivo(models.Model):
    id_resumen_ej = models.IntegerField(primary_key=True)
    resumen = models.CharField(max_length=45)
    id_entregable = models.ForeignKey(Entregables, null=False,
                                      blank=False, on_delete=models.CASCADE)


class ActividadesProyecto(models.Model):
    id_actividades_entr = models.IntegerField(primary_key=True)
    numero_actividad = models.IntegerField()
    descripcion_actividades_proy = models.CharField(max_length=45)
    alcance_actividades = models.CharField(max_length=45)
    observaciones_actividades = models.CharField(max_length=500)


class ObjetivosAlcanzados(models.Model):
    id_objetivos_alcanzados = models.IntegerField(primary_key=True)
    descripcion_obj_alcanzados = models.CharField(max_length=45)
    alcance_objetivos = models.CharField(max_length=45)
    observaciones_obj_alcanzados = models.CharField(max_length=500)
    id_entregable = models.ForeignKey(Entregables, null=False,
                                      blank=False, on_delete=models.CASCADE)


class MetasAlcanzadas(models.Model):
    id_metas_alcanzadas = models.IntegerField(primary_key=True)
    descripcion_metas_alcanzadas = models.CharField(max_length=45)
    alcance_metas_alcanzadas = models.CharField(max_length=45)
    observaciones_metas_alcanzadas = models.CharField(max_length=500)
    id_entregable = models.ForeignKey(Entregables, null=False,
                                      blank=False, on_delete=models.CASCADE)
