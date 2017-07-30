#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import admin
from django.db.models import Sum
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import DetalleFactura, Factura, Servicio, Socio, Proyecto, Zona, Manzana, Lote, SocioDeuda



#Admin Registro de socios
@admin.register(Socio)
class AdminSocio(admin.ModelAdmin):
	list_display = ('apellido', 'nombre', 'telefono', 'direccion','email', 'fecha_ingreso','get_ubicacion')
	search_fields = ['apellido','nombre']
	list_filter = ('apellido','nombre','fecha_ingreso')
	
	def get_ubicacion(self, obj):
		lote = Lote.objects.filter(socio__nombre=obj.nombre)
		manzana = Manzana.objects.filter(lote__socio__nombre=obj.nombre)
		proyecto = Proyecto.objects.filter(manzana__lote__socio__nombre=obj.nombre)
		print proyecto
		if len(lote) > 0 and len(lote) <= 1:
			#lotesito.manzana				
			#lotesito.id
			#lotesito.superficie
			return "Manzana {} lote {}".format(manzana[0],lote[0])
		elif len(lote) > 1 and len(lote) <= 2:
			return "Manzana {} lote {} proyecto {} y Manzana {} lote {} proyecto {}".format(manzana[0],lote[0],proyecto[0],manzana[1],lote[1],proyecto[1])
		else:
			return "Lote no asignado"
		
	get_ubicacion.short_description = 'Ubicación'

	



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

#Trabajando con la facturacion en el admin
class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura
    list_display = ['servicio', 'cantidad', 'descripcion',]


@admin.register(Factura)
class Factura(admin.ModelAdmin):
	model = Factura
	list_display = ['num_factura', 'socio', 'fecha','get_total']
	list_filter = ('socio',)
	inlines = (DetalleFacturaInline,)
	raw_id_fields = ('socio',)

	def get_total(self, obj):
		#total = DetalleFactura.objects.aggregate(Sum('valor', field="valor*cantidad"))
		print obj
		detalleFactura = DetalleFactura.objects.filter(factura__num_factura=obj.num_factura)
		total = ( detalleFactura.aggregate(
                total=Sum('valor', field='valor*cantidad')
             )['total']
         )
		return total

		
	get_total.short_description = 'Total'


@admin.register(Servicio)
class AdminZona(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)

#este funciona mostrar el importe pero no me funciona en el inline dentro de Factura si lo soluciono
#en DetalleFacturaInline esta clase desaparece
@admin.register(DetalleFactura)
class AdminDetalleFactura(admin.ModelAdmin):
	model = DetalleFactura
	list_display = ['servicio', 'importe', 'cantidad','numero_factura']
