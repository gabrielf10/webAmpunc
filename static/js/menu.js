$(document).ready(main);

var contador = 1;

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
	
	
	

};


