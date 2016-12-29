from django.shortcuts import render
from sistema.models import Socio, Lote, Proyecto, Factura
from django.template import loader # en vez de usar render para templates
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

import pdfkit
import datetime




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

#--------SOCIO--------------------------------
def sistema_socio(request):
	socios = Socio.objects.order_by('id')
	template = loader.get_template('sistema/socios.html')
	context = {
		'socios': socios,
		#variable url para controlar la class active en el html
		'url':'socio'
	}
	return HttpResponse(template.render(context, request))

#CLASS BASED VIEWS
class CrearSocioView(CreateView):
	model = Socio
	success_url = reverse_lazy('sistema:socio')
	fields = ['nombre', 'apellido', 'direccion', 'telefono', 'email','fecha_ingreso']

class EditarSocioView(UpdateView):
	model = Socio
	success_url = reverse_lazy('sistema:socio')
	fields = ['nombre', 'apellido', 'direccion', 'telefono', 'email','fecha_ingreso']

class EliminarSocioView(DeleteView):
	model = Socio
	template_name = "sistema/socio_delete.html"
	success_url = reverse_lazy('sistema:socio')
	fields = ['nombre', 'apellido', 'direccion', 'telefono', 'email','fecha_ingreso']

#-------FIN SOCIO ----------------------	

def sistema_socio_slug(request, slug):
    socio = Socio.objects.get(slug=slug)
    template = loader.get_template('sistema/socios_slug.html')
    context = {
		'socio': socio,
	}
    return HttpResponse(template.render(context, request))


def pdf(request):
	fecha = str(datetime.datetime.now())[:10]
	dt = datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime('%Y %m %d')
	pdf = pdfkit.from_url("http://127.0.0.1:8000/sistema/socios/", "socios%s.pdf" % fecha )
	return HttpResponse("Se genero el reporte")

#--------Facturacion--------------------------------
def sistema_facturacion(request):
	factura = Factura.objects.order_by('id')
	template = loader.get_template('sistema/facturacion.html')
	context = {
		'facturas': factura,
		#variable url para controlar la class active en el html
		'url':'factura'
	}
	return HttpResponse(template.render(context, request))