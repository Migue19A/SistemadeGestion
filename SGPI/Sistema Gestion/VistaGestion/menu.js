function menu(opcion, Inicio, PreRegistro, Seguimiento, Reporte, Prorrogas, Reactivacion, Cambio, GestionU, ConsultaP, Configuracion, Calendariza, HistorialP, HistorialD) {
    document.write("<div id='cssmenu' style='z-index:1'>");
    document.write("<ul>");
    if (opcion == 1) {
        document.write("<li class='active'><a href='" + Inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 3px;'></span>Inicio</a></li>");
    } else {
        document.write("<li class=''><a href='" + Inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 3px;'></span>Inicio</a></li>");
    }
    if (opcion == 2) {
        document.write("<li  class='active'><a href=''><span class='glyphicon glyphicon-send' style='margin-right: 3px;'></span>Solicitudes</a>");
    } else {
        document.write("<li ><a href=''><span class='glyphicon glyphicon-send' style='margin-right: 3px;'></span>Solicitudes</a>");
    }
    document.write(" <ul> ");
    document.write(" <li class=''><a href='" + PreRegistro + "'>Pre-registro</a></li>");
    document.write("<li class=''><a href='" + Prorrogas + "'><span class='' style='color: #fff'></span>Prórrogas</a> ");
    document.write("</li>");
    document.write("<li class=''><a href='" + Reactivacion + "'><span class='' style='color: #fff'></span>Reactivación de Proyectos</a> ");
    document.write(" </li>");
    document.write("<li class=''><a href='" + Cambio + "'>Gestión de Colaboradores</a>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
    if (opcion == 3) {
        document.write("<li  class='active'><a href=''><span class='glyphicon glyphicon-save-file' style='margin-right: 3px;'></span>Historial</a>");
    } else {
        document.write("<li ><a href=''><span class='glyphicon glyphicon-save-file' style='margin-right: 3px;'></span>Historial</a>");
    }
    document.write(" <ul> ");
    document.write(" <li class=''><a href='" + HistorialD + "'>Docentes</a></li>");
    document.write("<li class=''><a href='" + HistorialP + "'><span class='' style='color: #fff'></span>Proyectos</a> ");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
    if (opcion == 4) {
        document.write("<li class='active'><a href='" + Reporte + "'><span class='glyphicon glyphicon-list-alt' style='margin-right: 3px;'></span>Reportes</a></li>");
    } else {
        document.write("<li class=''><a href='" + Reporte + "'><span class='glyphicon glyphicon-list-alt' style='margin-right: 3px;'></span>Reportes</a></li>");
    }
    if (opcion == 5) {
        document.write("<li class='active'><a href='" + Calendariza + "'><span class='glyphicon glyphicon-calendar' style='margin-right: 3px;'></span>Calendarización</a></li>");
    } else {
        document.write("<li class=''><a href='" + Calendariza + "'><span class='glyphicon glyphicon-calendar' style='margin-right: 3px;'></span>Calendarización</a></li>");
    }
    if (opcion == 6) {
        document.write("<li class='active'><a href='" + Seguimiento + "'><span class='glyphicon glyphicon-arrow-right' style='margin-right: 3px;'></span>Seguimiento</a></li>");
    } else {
        document.write("<li class=''><a href='" + Seguimiento + "'><span class='glyphicon glyphicon-arrow-right' style='margin-right: 3px;'></span>Seguimiento</a></li>");
    }
    if (opcion == 7) {
        document.write("<li class='active'><a href='" + GestionU + "'><span class='glyphicon glyphicon-wrench' style='margin-right: 3px;'></span>Gestión de usuarios</a></li>");
    } else {
        document.write("<li class=''><a href='" + GestionU + "'><span class='glyphicon glyphicon-wrench' style='margin-right: 3px;'></span>Gestión de usuarios</a></li>");
    }
    if (opcion == 8) {
        document.write("<li class='active'><a href='" + ConsultaP + "'><span class='glyphicon glyphicon-search' style='margin-right: 3px;'></span>Concentrado de proyectos</a></li>");
    } else {
        document.write("<li class=''><a href='" + ConsultaP + "'><span class='glyphicon glyphicon-search' style='margin-right: 3px;'></span>Concentrado de proyectos</a></li>");
    }
    if (opcion == 9) {
        document.write("<li style='float: right;' class='active'");
        document.write("class='active'><a href=''><span class='glyphicon glyphicon-user' style='margin-right: 3px;'></span>Oficina de Seguimiento de <br> Proyectos de Investigación</a>");
    } else {
        document.write("<li style='float: right;' class='has-sub'");
        document.write("class='active'><a href=''><span class='glyphicon glyphicon-user' style='margin-right: 3px;'></span>Oficina de Seguimiento de <br>&nbsp;&nbsp;&nbsp;&nbsp; Proyectos de Investigación</a>");
    }
    document.write(" <ul> ");
    document.write("<li class=''><a href=''><span class='glyphicon glyphicon-remove-circle' style='color: #fff; margin-right: 10px;'></span>Cerrar Sesión</a> ");
    document.write("</li>");
    document.write("<li class=''><a href='" + Configuracion + "'><span class='glyphicon glyphicon-wrench' style='color: #fff; margin-right: 10px;'></span>Configuración</a> ");
    document.write(" </li>");
    document.write("</ul>");
    document.write("</li>");
    document.write("</div>");
}