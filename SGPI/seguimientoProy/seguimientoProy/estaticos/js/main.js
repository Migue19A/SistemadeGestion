$(document).ready(function(){
	$('ul.tabs li a:first').addClass('actives');
	$('.seccionesS article').hide();
	$('.seccionesS article:first').show();

	$('ul.tabs li a').click(function(){
		$('ul.tabs li a').removeClass('actives');
		$(this).addClass('actives');
		$('.seccionesS article').hide(); 

		var activeTab3 = $(this).attr('href');
		$(activeTab3).show();
		return false;

	});

	$('.container a').click(function(){
		$('ul.tabs li a').removeClass('actives');
		$('.seccionesS article').hide(); 
		
		var activeTab4 = $(this).attr('href');
		$(activeTab4).show();
		return false;

	});
});

