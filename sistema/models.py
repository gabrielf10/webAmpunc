#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinValueValidator
from decimal import *
#from sistema import utilerias


class Socio(models.Model):
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	slug = models.SlugField(
	max_length=60, blank=True, null=True, editable=False)	
	direccion = models.CharField(max_length=255)
	telefono = models.PositiveIntegerField(unique=True)
	email = models.EmailField(max_length=255)
	fecha_ingreso = models.DateField()
	def save(self, **kwargs):
		slug_str = "%s" % (self.nombre)
		#utilerias.unique_slugify(self, slug_str)
		super(Socio, self).save(**kwargs)

	def get_absolute_url(self):
		return reverse('noticias-etiqueta-list', args=[self.slug])

	def __unicode__(self):
		return self.nombre
			
	class Meta:
		ordering = ('id',)

def increment_numero_factura():
		last_invoice = Factura.objects.all().order_by('id').last()
		if not last_invoice:
			return 'MAG0001'
		num_factura = last_invoice.num_factura
		invoice_int = int(num_factura.split('MAG')[-1])
		new_invoice_int = invoice_int + 1
		new_invoice_no = 'MAG' + str(new_invoice_int)
		return new_invoice_no

def _calcular_total(self):
	return self.cantidad*(servicio.importe)
	total = property(_calcular_total)
	
class Factura(models.Model):
	#num_factura = models.PositiveIntegerField(unique=True)
	num_factura = models.CharField(max_length = 500, default = increment_numero_factura, null = True, blank = True)
	socio = models.ForeignKey(Socio)
	fecha = models.DateField() 
	def __unicode__(self):
		return self.num_factura

class Servicio(models.Model):
	nombre = models.CharField(max_length=100)
	importe = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	def __unicode__(self):
		return self.nombre

class DetalleFactura(models.Model):
	factura = models.ForeignKey(Factura)
	servicio = models.ForeignKey(Servicio)
	cantidad = models.DecimalField(max_digits=6, decimal_places=0, validators=[MinValueValidator(Decimal('0.01'))])
	subtotal = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	descripcion = models.CharField(verbose_name="Descripción", max_length=100, help_text="Descripción del servicio.")

	def _get_importe(self):
		return self.cantidad*self.subtotal

	importe = property(_get_importe)

	def  __unicode__(self):
		return self.servicio.nombre

class Zona(models.Model):
	nombre = models.CharField(max_length=255)
	def __unicode__(self):
		return self.nombre

class Proyecto(models.Model):
	nombre = models.CharField(max_length=255)
	zona = models.ForeignKey(Zona)
	direccion = models.CharField(max_length=255)
	valor_m2_terreno = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	valor_m2_urbanizacion = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	fecha_inicio = models.DateField()
	actualizacion = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ('id',)

class Manzana(models.Model):
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,)
	nombre = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ('id',)

class Lote(models.Model):
	numero = models.CharField(max_length=3)
	manzana = models.ForeignKey(Manzana, on_delete=models.CASCADE,)
	superficie = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	ocupado = models.BooleanField(default=False)
	#no es obligatoria
	socio = models.ForeignKey(Socio, blank=True, null=True)

	def __unicode__(self):
		return str(self.numero)
	class Meta:
		ordering = ('id',)

class Deuda(models.Model):
	nombre = models.CharField(max_length=255)
	importe = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

class SocioDeuda(models.Model):
	socio = models.ForeignKey(Socio)
	deuda = models.ForeignKey(Deuda)
	cantidad = models.PositiveIntegerField()





