#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import DetalleFactura, Factura, Servicio, Socio, Proyecto, Zona, Manzana, Lote, SocioDeuda
	
#Admin Registro de socios
@admin.register(Socio)
class AdminSocio(admin.ModelAdmin):
	list_display = ('apellido', 'nombre', 'telefono', 'direccion','email', 'fecha_ingreso','get_lote','get_manzana','get_proyecto')
	list_filter = ('apellido','nombre','fecha_ingreso')
	
	def get_lote(self, obj):
		lote = obj.lote_set.all			 
			#lotesito.manzana				
			#lotesito.id
			#lotesito.superficie
		
		return lote
	get_lote.short_description = 'lote'

	def get_manzana(self, obj):
		return obj.id
		
	def get_proyecto(self, obj):
		return obj.id



#Admin Registro de Zonas del proyecto
@admin.register(Zona)
class AdminZona(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)

#Admin nested Inline Para registro de Proyecto Manzanas y Lotes en una sola pantalla
#https://pypi.python.org/pypi/django-nested-inline/0.3.6 Funcionando
class AdminLotes(NestedStackedInline):
	list_display = ('manzana','id','superficie','ocupado')
	list_filter = ('manzana', 'id', 'ocupado','socio')
	model = Lote 
	extra = 1 
	fk_name = 'manzana'

class AdminManzana(NestedStackedInline):
	list_display = ('nombre','proyecto')
	model = Manzana 
	extra = 1
	fk_name = 'proyecto' 
	inlines = [AdminLotes]

@admin.register(Proyecto)
class AdminProyecto(NestedModelAdmin):
	list_display = ('nombre','zona','direccion','fecha_inicio')
	list_filter = ('nombre','zona','fecha_inicio',)
	model = Proyecto 
	inlines = [AdminManzana]
#Fin Nested Inline

class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura

@admin.register(Factura)
class Factura(admin.ModelAdmin):
    inlines = (DetalleFacturaInline,)

@admin.register(Servicio)
class AdminZona(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)

