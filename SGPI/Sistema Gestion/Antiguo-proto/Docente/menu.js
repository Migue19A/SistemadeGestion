function menu(opcion, Inicio, NPreRegistro, PreRegistros, Prorrogas, Seguimiento, CambioColaborador, CProyectos, ProyectosCancelados, ConfiCuenta,HistorialD) {
    document.write("<div id='cssmenu' style='z-index:1'>");
    document.write("<ul>");
    if (opcion == 1) {
        document.write("<li class='active'><a href='" + Inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 10px;'></span>Inicio</a></li>");
    } else {
        document.write("<li class=''><a href='" + Inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 10px;'></span>Inicio</a></li>");
    }
    if (opcion == 2) {
        document.write(" <li class='active'><a href=''><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Registrar Proyectos</a>");
    } else {
        document.write(" <li ><a href='#'><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Pre-Registros</a>");
    }
    document.write("<ul>");
    document.write("<li> <a href='" + NPreRegistro + "'>Nuevo</a> </li>");
    document.write("</li>");
    document.write("<li class=''><a href='" + PreRegistros + "'>Concentrado</a>");
    document.write("</li>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
        if (opcion == 4) {
        document.write("<li  class='active'><a href='" + CProyectos + "'><span class='glyphicon glyphicon-book' style='margin-right: 10px;'></span>Concentrado de proyectos</a>");
    } else {
        document.write("<li ><a href='" + CProyectos + "'><span class='glyphicon glyphicon-book' style='margin-right: 10px;'></span>Concentrado de proyectos</a>");
    }
    if (opcion == 3) {
        document.write("<li class='active'><a href='" + Seguimiento + "'><span class='glyphicon glyphicon-arrow-right' style='margin-right: 10px;'></span>Seguimiento</a>");
    } else {
        document.write("<li class=''><a href='" + Seguimiento + "'><span class='glyphicon glyphicon-arrow-right' style='margin-right: 10px;'></span>Seguimiento</a>");
    }
    if (opcion == 6) {
        document.write("<li class='active'><a href=" + Prorrogas + "><span class='glyphicon glyphicon-plus' style='margin-right: 10px;'></span>Prórrogas</a></li>");
    } else {
        document.write("<li class=''><a href=" + Prorrogas + "><span class='glyphicon glyphicon-plus' style='margin-right: 10px;'></span>Prórrogas</a></li>");
    }
    document.write("</li>");
    if (opcion == 5) {
        document.write("<li class='active'><a href='" + CambioColaborador + "'><span class='glyphicon glyphicon-remove-circle' style='margin-right: 10px;'></span>Gestión de Colaboradores</a></li>");
    } else {
        document.write("<li><a href='" + CambioColaborador + "'><span class='glyphicon glyphicon-remove-circle' style='margin-right: 10px;'></span>Gestión de Colaboradores</a></li>");
    }
    if (opcion == 7) {
        document.write("<li  class='active'><a href='" + HistorialD + "'><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Historial</a>");
    } else {
        document.write("<li ><a href='" + HistorialD + "'><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Historial</a>");
    }

    document.write("<li style='float: right;' class='has-sub'");
    document.write("<li><a href='#'><span class='glyphicon glyphicon-user' style='margin-right: 10px;'></span>Docente Responsable</a>");
    document.write(" <ul>");
    document.write("<li><a href='float: right;'><span class='glyphicon glyphicon-remove-circle' style='margin-right: 10px;'></span>Cerrar Sesión</a></li>");
    document.write("<li><a href='" + ConfiCuenta + "'><span class='glyphicon glyphicon-wrench' style=' margin-right: 10px;'></span>Configuración</a></li>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</div>");
}