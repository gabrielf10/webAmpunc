# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit

# Create your models here.

class Proyecto(models.Model):
	titulo = models.CharField(max_length=200)
	url = models.ImageField(upload_to='img', verbose_name='Imágen')
	imagen = ImageSpecField(source='url',
							processors=[ResizeToFit(700,700)],
							format='JPEG',
							options={'quality':80})
	
	imagen_miniatura = ImageSpecField(source='url',
							processors=[ResizeToFill(50,50)],
							format='JPEG',
							options={'quality':80})
	subtitulo = models.CharField(max_length=200)
	descripcion_izq = models.TextField(verbose_name = 'Descripcion Izquierda')
	descripcion_der = models.TextField(verbose_name = 'Descripcion Derecha')

	def __unicode__(self):
		return self.titulo
	class Meta:
		verbose_name_plural='Proyectos'	


class ImagenesSlide(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	url = models.ImageField(upload_to='img', verbose_name='Imágen')
	imagen = ImageSpecField(source='url',
							processors=[ResizeToFit(1600,500)],
							format='JPEG',
							options={'quality':80})
	
	imagen_miniatura = ImageSpecField(source='url',
							processors=[ResizeToFill(100,50)],
							format='JPEG',
							options={'quality':80})

	def __unicode__(self):
		return self.nombre
	class Meta:
		verbose_name_plural='Imagenes Slide Portada'