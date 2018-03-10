function menu(opcion, inicio, Re, Seg, Pro, Rea, HistorialD, HistorialP) {
    document.write("<div id='cssmenu' style='z-index:1'>");
    document.write("<ul>");
    if (opcion == 1) {
        document.write("<li class='active'><a href='" + inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 10px;'></span>Inicio</a></li>");
    } else {
        document.write("<li class=''><a href='" + inicio + "'><span class='glyphicon glyphicon-home' style='margin-right: 10px;'></span>Inicio</a></li>");
    }
    if (opcion == 2) {
        document.write("<li class='active'><a href='" + Re + "'><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Solicitudes</a>");
    } else {
        document.write("<li class=''><a href='" + Re + "'><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Solicitudes</a>");
    }
    document.write("<ul>");
    document.write("<li class=''><a href='" + Re + "'>Registro</a></li>");
    document.write("<li class=''><a href='" + Pro + "'>Prórrogas</a>");
    document.write("<li><a href='" + Rea + "'>Reactivación</a>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
    if (opcion == 3) {
        document.write("<li class='active'><a href=''><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Historial</a>");
    } else {
        document.write("<li class=''><a href=''><span class='glyphicon glyphicon-save-file' style='margin-right: 10px;'></span>Historial</a>");
    }
    document.write("<ul>");
    document.write("<li class=''><a href='" + HistorialP + "'>Docentes</a></li>");
    document.write("<li class=''><a href='" + HistorialD + "'>Proyectos</a>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</li>");
    if (opcion == 4) {
        document.write("<li class='active'><a href='" + Seg + "'><span class='glyphicon glyphicon-file' style='margin-right: 10px;'></span>Seguimiento de etapas</a></li>");
    } else {
        document.write("<li class=''><a href='" + Seg + "'><span class='glyphicon glyphicon-file' style='margin-right: 10px;'></span>Seguimiento de etapas</a></li>");
    }
    document.write("<li style='float: right;' class='has-sub'>");
    document.write("<a href='#'><span class='glyphicon glyphicon-user' style='margin-right: 10px;'></span>Consejo de Investigación</a>");
    document.write(" <ul>");
    document.write("<li><a href='#'><span class='glyphicon glyphicon-remove-circle' style='margin-right: 10px;'></span>Cerrar Sesión</a></li>");
    document.write("<li><a href='#'><span class='glyphicon glyphicon-wrench' style=' margin-right: 10px;'></span>Configuración</a></li>");
    document.write("</ul>");
    document.write("</li>");
    document.write("</ul>");
    document.write("</div>");
}