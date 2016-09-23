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
	proyecto = models.ForeignKey(Proyecto)
	nombre = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre
	class Meta:
		ordering = ('id',)

class Lote(models.Model):
	manzana = models.ForeignKey(Manzana)
	superficie = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
	ocupado = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.id)
	class Meta:
		ordering = ('id',)





