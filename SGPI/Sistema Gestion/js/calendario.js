function calendar()
{
document.write("<div class='col-lg-3' id='panelIzquierdo'>               <div class='panel panel-default' id='notificaciones'>                 <div align='center' class='panel-heading'>                     <h5>                         Notificaciones                     </h5>                 </div>                 <div class='panel-body' id='ContNotif'>                     <div class='alert alert-success alert-dismissable fade in' id='#notificacion'>                         <a aria-label='close' class='close' data-dismiss='alert' href='#'>                             ×                         </a>                         <h5 class='item-title'>                             El proyecto 'Pelador de Chayotes'  ha sido aceptado                         </h5>                         <a class='item-info'>                             <h6>                                 Ver en seguimiento de proyectos                             </h6>                         </a>                     </div>                     <div class='alert alert-success alert-dismissable fade in' id='#notificacion'>                         <a aria-label='close' class='close' data-dismiss='alert' href='#'>                             ×                         </a>                         <h5 class='item-title'>                             La prórroga de la etapa 2 del proyecto 'Hamburguesa' ha sido aceptada                         </h5>                         <a class='item-info'>                             <h6>                                 Consultar nueva fecha de entrega en seguimiento de proyectos                             </h6>                         </a>                     </div>                     <div class='alert alert-danger alert-dismissable fade in' id='#notificacion'>                         <a aria-label='close' class='close' data-dismiss='alert' href='#'>                             ×                         </a>                         <h5 class='item-title'>                             Faltan 3 días para la entrega de reporte del Proyecto Comida Enlatada                         </h5>                         <a class='item-info'>                             <h6>                                 Realizar entrega en seguimiento de proyectos                             </h6>                         </a>                     </div>                     <div class='alert alert-success alert-dismissable fade in' id='#notificacion'>                         <a aria-label='close' class='close' data-dismiss='alert' href='#'>                             ×                         </a>                         <h5 class='item-title'>                             El proyecto 'Pelador de Chayotes' ha sido aceptado                         </h5>                         <a class='item-info'>                             <h6>                                 Ver en seguimiento de proyectos                             </h6>                         </a>                     </div>                     <div class='alert alert-success alert-dismissable fade in' id='#notificacion'>                         <a aria-label='close' class='close' data-dismiss='alert' href='#'>                             ×                         </a>                         <h5 class='item-title'>                             La prórroga de la etapa 2 del proyecto 'Hamburguesa' ha sido aceptada                         </h5>                         <a class='item-info'>                             <h6>                                 Consultar nueva fecha de entrega en seguimiento de proyectos                             </h6>                         </a>                     </div>                     <div class='alert alert-danger alert-dismissable fade in' id='#notificacion'>                         <a aria-label='close' class='close' data-dismiss='alert' href='#'>                             ×                         </a>                         <h5 class='item-title'>                             Faltan 3 días para la entrega de reporte del Proyecto Comida Enlatada                         </h5>                         <a class='item-info'>                             <h6>                                 Realizar entrega en Seguimiento de Proyectos                             </h6>                         </a>                     </div>                 </div>                 <div class='panel panel-default' id='calendarioPeq'>                     <div align='center' class='panel-heading'>                         <h5>                             Calendario                         </h5>                     </div>                                          <div style='overflow:hidden;'>                         <div id='calendar_div'>                             <div id='calender_section'>                                 <div class='none' id='event_list'>                                 </div>                                 <div id='calender_section_top'>                                     <ul>                                         <li>                                             Dom                                         </li>                                         <li>                                             Lun                                         </li>                                         <li>                                             Mart                                         </li>                                         <li>                                             Miérc                                         </li>                                         <li>                                             Juev                                         </li>                                         <li>                                             Vier                                         </li>                                         <li>                                             Sáb                                         </li>                                     </ul>                                 </div>                                 <div id='calender_section_bot'>                                     <ul>                                         <li>                                             <span>                                             </span>                                         </li>                                         <li>                                             <span>                                             </span>                                         </li>                                         <li>                                             <span>                                             </span>                                         </li>                                         <li>                                             <span>                                             </span>                                         </li>                                         <li>                                             <span>                                             </span>                                         </li>                                         <li class='date_cell' style='background: red;' date='2017-09-1'>                                             <span>                                                 1                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-1'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Solicitud de prórroga                                                     </div>                                                     <a href='javascript:;' onclick='getEvents('2017-09-1');'>                                                         Ver Eventos                                                     </a>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-2'>                                             <span>                                                 2                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-2'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-3'>                                             <span>                                                 3                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-3'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' style='background: #7FC1FF;' date='2017-09-4'>                                             <span>                                                 4                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-4'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                        Cambio de Colaborador                                                                                      </div>                <a href='javascript:;' onclick='getEvents('2017-09-4');'>Ver eventos</a>                                  </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-5'>                                             <span>                                                 5                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-5'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-6'>                                             <span>                                                 6                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-6'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-7'>                                             <span>                                                 7                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-7'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-8'>                                             <span>                                                 8                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-8'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-9'>                                             <span>                                                 9                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-9'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-10'>                                             <span>                                                 10                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-10'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-11'>                                             <span>                                                 11                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-11'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-12'>                                             <span>                                                 12                                             </span> ");
document.write("<div class='date_popup_wrap none' id='date_popup_2017-09-12'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-13'>                                             <span>                                                 13                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-13'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-14'>                                             <span>                                                 14                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-14'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-15'>                                             <span>                                                 15                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-15'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-16'>                                             <span>                                                 16                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-16'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-17'>                                             <span>                                                 17                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-17'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-18'>                                             <span>                                                 18                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-18'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-19'>                                             <span>                                                 19                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-19'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-20'>                                             <span>                                                 20                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-20'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-21'>                                             <span>                                                 21                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-21'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-22'>                                             <span>                                                 22                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-22'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-23'>                                             <span>                                                 23                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-23'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-24'>                                             <span>                                                 24                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-24'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-25'>                                             <span>                                                 25                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-25'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-26'>                                             <span>                                                 26                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-26'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-27'>                                             <span>                                                 27                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-27'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-28'>                                             <span>                                                 28                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-28'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-29'>                                             <span>                                                 29                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-29'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                         <li class='date_cell' date='2017-09-30'>                                             <span>                                                 30                                             </span>                                             <div class='date_popup_wrap none' id='date_popup_2017-09-30'>                                                 <div class='date_window'>                                                     <div class='popup_event'>                                                         Events (0)                                                     </div>                                                 </div>                                             </div>                                         </li>                                     </ul>                                 </div>                             </div>  ");
document.write("<script type='text/javascript'>                                 function getCalendar(target_div,year,month) 	                            { 								    $.ajax( 								    { 								        type:'POST', 								        url:'functions.php', 								        data:'func=getCalender&year='+year+'&month='+month, 								        success:function(html){ 								          $('#'+target_div).html(html); 								        } 								      }); 								    } 								    function getEvents(date) 								    { 								      $.ajax({ 								        type:'POST', 								        url:'functions.php', 								        data:'func=getEvents&date='+date, 								        success:function(html){ 								          $('#event_list').html(html); 								          $('#event_list').slideDown('slow'); 								        } 								      }); 								    } 								    function addEvent(date) 								    { 								      $.ajax({ 								        type:'POST', 								        url:'functions.php', 								        data:'func=addEvent&date='+date, 								        success:function(html){ 								          $('#event_list').html(html); 								          $('#event_list').slideDown('slow'); 								        } 								      }); 								    } 								    $(document).ready(function(){ 								      $('.date_cell').mouseenter(function(){ 								        date = $(this).attr('date'); 								        $('.date_popup_wrap').fadeOut(); 								        $('#date_popup_'+date).fadeIn();   								      }); 								      $('.date_cell').mouseleave(function(){ 								        $('.date_popup_wrap').fadeOut();     								      }); 								      $('.month_dropdown').on('change',function(){ 								        getCalendar('calendar_div',$('.year_dropdown').val(),$('.month_dropdown').val()); 								      }); 								      $('.year_dropdown').on('change',function(){ 								        getCalendar('calendar_div',$('.year_dropdown').val(),$('.month_dropdown').val()); 								      }); 								      $(document).click(function(){ 								        $('#event_list').slideUp('slow'); 								      }); 						    	});                             </script>                         </div>                     </div>                 </div>             </div>         </div>");
}