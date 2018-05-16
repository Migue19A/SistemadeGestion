# Sistema de Gestion y Seguimiento de Proyectos

Repositorio para el proyecto.

##para poder ejecutarlo necesitas:
    *instalar PostgreSQL
    *instalar python.
    *instalar pip.
    *crear un ambiente virtual
    *instalar django en el ambiente virtual.
    *instalar las dependencias de INSTALLED_APP se settings.py


##instalando python
    https://www.python.org/downloads/

    instalar version 3.6.4 y en el asistente de instalación agregar python al PATH

##instalacion de PIP
    una vez instalado python hay que instalar su gestor de paquetes

    hay que descargar pip desde https://bootstrap.pypa.io/get-pip.py
    clic derecho sobre la pagina y guardar como. esto descargara un archivo .py
    solo hay que ejecutarlo con

    python get-pip.py

##instalacion del ambiente virtual
    seguir los pasos de 
    
    http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

    menos la sección donde coloca el PATH de python en las variables de entorno

##instalar los paquetes necesarios
    dentro de la ubicación del entorno virtual instalar los paquetes de pip
    necesarios para la ejecución del programa
    **lista pendiente

#las inserciones están en la raíz del repositorio. Por lógica van a saber a qué tabla pertenece cada archivo,
se actualizó el modelo, tienen que hacer de nuevo la migración. Borren mi superusuario y creen uno ustedes