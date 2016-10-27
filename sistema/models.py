#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MinValueValidator
from decimal import *


class Socio(models.Model):
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	telefono = models.PositiveIntegerField(unique=True)
	email = models.EmailField(max_length=255)
	fecha_ingreso = models.DateField()

	def __unicode__(self):
		return self.nombre
			
	class Meta:
		ordering = ('id',)

	
class Factura(models.Model):
	num_factura = models.PositiveIntegerField(unique=True)
	socio = models.ForeignKey(Socio)
	cantidad = models.PositiveIntegerField()
	interes = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	def _calcular_total(self):
		return self.cantidad*(servicio.importe)
	total = property(_calcular_total)

class Servicio(models.Model):
	factura = models.ForeignKey(Factura)
	nombre = models.CharField(max_length=100)
	importe = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	descripcion = models.CharField(verbose_name="Descripción", max_length=100, help_text="Descripción del servicio.")
	def __unicode__(self):
		return self.nombre

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
	socio = models.ForeignKey(Socio)

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





