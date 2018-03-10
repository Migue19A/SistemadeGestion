function notif()
{
//document.write("<script type='text/javascript' >");
document.write(" $(document).ready(function()");
document.write("{");
document.write("$'#notificationLink').click(function()");
document.write("{");
document.write("$('#notificationContainer').fadeToggle(300);");
document.write("$('#notification_count').fadeOut('slow');");
document.write("return false;");
document.write("})");

//Document Click
document.write("$(document).click(function()");
document.write("{");
//$("#notificationContainer").hide();
document.write("});");
//Popup Click
document.write("$('#notificationContainer').click(function()");
document.write("{");
//return false
document.write("});");

document.write("});");
//document.write("</script>");
}