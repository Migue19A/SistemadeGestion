function menu(opcion, Inicio, Registros, Etapas, Prorrogas, Reactivacion, CambioColaborador, CProyectos, ConfiCuenta, Reportes, HistorialD, HistorialP,GestionU) {
    document.write("<div id='cssmenu' style='z-index:1'>");
    document.write("<ul>");
    if (opcion == 1) {
        document.write("<li class='active'><a href='" + Inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 10px;'></span>Inicio</a></li>");
    } else {
        document.write("<li class=''><a href='" + Inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 10px;'></span>Inicio</a></li>");
    }
    if (opcion == 2) {
        document.write("<li  class='active'><a href='#'><span class='glyphicon glyphicon-send' style='margin-right: 10px;'></span>Solicitudes</a>");
    } else {
        document.write("<li ><a href='#'><span class='glyphicon glyphicon-send' style='margin-right: 10px;'></span>Solicitudes</a>");
    }
    document.write(" <ul> ");
    document.write(" <li class=''><a href='" + Registros + "'>Registro</a>");
    document.write("</li>");
    document.write("<li class=''><a href='" + Prorrogas + "'><span class='' style='color: #fff'></span>Prórrogas</a> ");
    document.write("</li>");
    document.write("<li class=''><a href='" + Reactivacion + "'><span class='' style='color: #fff'></span>Reactivación  </a> ");
    document.write(" </li>");
    document.write("<li class=''><a href='" + CambioColaborador + "'><span class='' style='color: #fff'></span>Gestión de Colaboradores</a>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
    if (opcion == 3) {
        document.write("<li  class='active'><a href='#'><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Historial</a>");
    } else {
        document.write("<li ><a href='#'><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Historial</a>");
    }
    document.write(" <ul> ");
    document.write(" <li class=''><a href='" + HistorialP + "'>Docente</a>");
    document.write("</li>");
    document.write("<li class=''><a href='" + HistorialD + "'><span class='' style='color: #fff'></span>Proyectos</a> ");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
    if (opcion == 4) {
        document.write("<li class='active'><a href='" + Reportes + "'><span class='glyphicon glyphicon-list-alt' style='margin-right: 10px;'></span>Reportes</a></li>");
    } else {
        document.write("<li class=''><a href='" + Reportes + "'><span class='glyphicon glyphicon-list-alt' style='margin-right: 10px;'></span>Reportes</a></li>");
    }
    if (opcion == 5) {
        document.write("<li class='active'><a href='" + Etapas + "'><span class='glyphicon glyphicon-arrow-right' style='margin-right: 10px;'></span>Seguimiento</a></li>");
    } else {
        document.write("<li class=''><a href='" + Etapas + "'><span class='glyphicon glyphicon-arrow-right' style='margin-right: 10px;'></span>Seguimiento</a></li>");
    }
    if (opcion == 6) {
        document.write("<li class='active'><a href='" + CProyectos + "'><span class='glyphicon glyphicon-search' style='margin-right: 10px;'></span>Concentrado de Proyectos</a></li>");
    } else {
        document.write("<li><a href='" + CProyectos + "'><span class='glyphicon glyphicon-search' style='margin-right: 10px;'></span>Concentrado de Proyectos</a></li>");
    }
    if (opcion == 7) {
        document.write("<li class='active'><a href='" + GestionU + "'><span class='glyphicon glyphicon-wrench' style='margin-right: 3px;'></span>Gestión de usuarios</a></li>");
    } else {
        document.write("<li class=''><a href='" + GestionU + "'><span class='glyphicon glyphicon-wrench' style='margin-right: 3px;'></span>Gestión de usuarios</a></li>");
    }
    if (opcion == 8) {
        document.write("<li style='float: right;' class='active'");
        document.write("class='active'><a href='#'><span class='glyphicon glyphicon-book' style='margin-right: 10px;'></span>Subdirección de Investigación y Posgrado</a>");
    } else {
        document.write("<li style='float: right;' class='has-sub'");
        document.write("class='active'><a href='#'><span class='glyphicon glyphicon-user' style='margin-right: 10px;'></span>Subdirección de Investigación y Posgrado</a>");
    }
    document.write(" <ul> ");
    document.write("<li class=''><a href='#'><span class='glyphicon glyphicon-remove-circle' style='color: #fff; margin-right: 10px;'></span>Cerrar Sesión</a> ");
    document.write("</li>");
    document.write("<li class=''><a href='" + ConfiCuenta + "'><span class='glyphicon glyphicon-wrench' style='color: #fff; margin-right: 10px;'></span>Configuración</a> ");
    document.write(" </li>");
    document.write("</ul>");
    document.write("</li>");
    document.write("</div>");
}