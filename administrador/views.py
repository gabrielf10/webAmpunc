from django.shortcuts import render
from administrador.models import Proyecto, ImagenesSlide
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext


# Create your views here.
def inicio(request):
	imagenes = ImagenesSlide.objects.all()
	proyectos = Proyecto.objects.all()
	return render_to_response('index.html',{'imagenes':imagenes, 'proyectos':proyectos}, RequestContext(request))

def proyectos(request):
	proyectos = Proyecto.objects.all()
	return render_to_response('proyectos.html',{'proyectos':proyectos}, RequestContext(request))

def encuesta(request):
	proyectos = Proyecto.objects.all()
	return render_to_response('encuesta.html',{'proyectos':proyectos}, RequestContext(request))

def institucional(request):
	proyectos = Proyecto.objects.all()
	return render_to_response('institucional.html',{'proyectos':proyectos}, RequestContext(request))

def contacto(request):
	return render_to_response('contacto.html', RequestContext(request))