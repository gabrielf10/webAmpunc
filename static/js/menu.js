$(document).ready(main);

var contador = 1;
$(function(){
		  $(".slides").slidesjs({
		    play: {
		      active: false,
		        // [boolean] Generate the play and stop buttons.
		        // You cannot use your own buttons. Sorry.
		      effect: "slide",
		        // [string] Can be either "slide" or "fade".
		      interval: 4000,
		        // [number] Time spent on each slide in milliseconds.
		      auto: true,
		        // [boolean] Start playing the slideshow on load.
		      swap: true,
		        // [boolean] show/hide stop and play buttons
		      pauseOnHover: false,
		        // [boolean] pause a playing slideshow on hover
		      restartDelay: 2500
		        // [number] restart delay on inactive slideshow
		    }
		  });
		});

function main(){
	
	/* boton al cielo */
	$('.ir-arriba').click(function(){
		$('body, html').animate({
			scrollTop: '0px'
		}, 300);
	});
 
	$(window).scroll(function(){
		if( $(this).scrollTop() > 300 ){
			$('.ir-arriba').slideDown(300);
		} else {
			$('.ir-arriba').slideUp(300);
		}
	});

	/* clase active para colorear el menu */	
    $('.menu li a').click(function(){

        $('.menu li a').removeClass('active'); // remove the class from the currently selected
        $(this).addClass('active'); // add the class to the newly clicked link
        /* para obtener la ruta del navegador sin el dominiovar pathname = window.location.pathname;
        alert(pathname);*/

    });


	$('.menu_bar').click(function(){
		//$('nav').toggle();
		if(contador==1){
			$('nav').animate({
				right: '0'
			});
			contador = 0;
		}else{
			$('nav').animate({
				right: '-100%'
			});
			contador = 1;
		}
	});

	/* Funcion para el filtro en las tablas del sistema */
	$(".search").keyup(function () {
    var searchTerm = $(".search").val();
    var listItem = $('.results tbody').children('tr');
    var searchSplit = searchTerm.replace(/ /g, "'):containsi('")
    
	$.extend($.expr[':'], {'containsi': function(elem, i, match, array){
	    return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
	}
	});

	$(".results tbody tr").not(":containsi('" + searchSplit + "')").each(function(e){
	$(this).attr('visible','false');
	});

	$(".results tbody tr:containsi('" + searchSplit + "')").each(function(e){
	$(this).attr('visible','true');
	});

	var jobCount = $('.results tbody tr[visible="true"]').length;
	$('.counter').text(jobCount + ' items encontrados');

	if(jobCount == '0') {$('.no-result').show();}
	else {$('.no-result').hide();}
	  });


};


