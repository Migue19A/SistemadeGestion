$(document).ready(function(){
	$('ul.tabs li a:first').addClass('actives');
	$('.secciones article').hide();
	$('.secciones article:first').show();

	$('ul.tabs li a').click(function(){
		$('ul.tabs li a').removeClass('actives');
		$(this).addClass('actives');
		$('.secciones article').hide(); 

		var activeTab = $(this).attr('href');
		$(activeTab).show();
		return false;

	});

	$('.container a').click(function(){
		$('ul.tabs li a').removeClass('actives');
		$('.secciones article').hide(); 
		
		var activeTab2 = $(this).attr('href');
		$(activeTab2).show();
		return false;

	});
});

