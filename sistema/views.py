from django.shortcuts import render
from sistema.models import Socio, Lote, Proyecto
from django.template import loader # en vez de usar render para templates
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def sistema_inicio(request):
	proyectos = Proyecto.objects.order_by('id')
	template = loader.get_template('sistema/proyectos.html')
	context = {
		'proyectos': proyectos, 
		#variable url para controlar la class active en el html
		'url':'proyectos'
	}
	return HttpResponse(template.render(context, request))
	#socios = Socio.objects.all()
	#lotes = Socio.objects.all()
	#return render_to_response('sistema/proyectos.html',{'socios':socios, 'lotes':lotes}, RequestContext(request))
def sistema_socio(request):
	socios = Socio.objects.order_by('id')
	template = loader.get_template('sistema/socios.html')
	context = {
		'socios': socios,
		#variable url para controlar la class active en el html
		'url':'socio'
	}
	return HttpResponse(template.render(context, request))

def sistema_socio_slug(request, slug):
    socio = Socio.objects.get(slug=slug)
    template = loader.get_template('sistema/socios_slug.html')
    context = {
		'socio': socio,
	}
    return HttpResponse(template.render(context, request))