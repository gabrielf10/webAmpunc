from django.contrib import admin
from .models import Socio, Proyecto, Zona, Manzana, Lote

#Aca modificar para registrar el modelo en el admin
@admin.register(Socio)
class AdminSocio(admin.ModelAdmin):
	list_display = ('apellido', 'nombre', 'telefono', 'direccion','email', 'fecha_ingreso')
	list_filter = ('apellido','nombre','fecha_ingreso')


class LoteInline(admin.StackedInline):
	model = Lote
	extra = 5

class ManzanaInline(admin.StackedInline):
	model = Manzana
	extra = 1
	
@admin.register(Proyecto)
class AdminProyecto(admin.ModelAdmin):
	list_display = ('nombre','zona','direccion','fecha_inicio')
	inlines = [ManzanaInline]
	list_filter = ('nombre','zona','fecha_inicio',)

@admin.register(Zona)
class AdminZona(admin.ModelAdmin):
	list_display = ('nombre',)
	list_filter = ('nombre',)


@admin.register(Manzana)
class AdminManzana(admin.ModelAdmin):
	list_display = ('nombre','proyecto')
	inlines = [LoteInline]

@admin.register(Lote)
class AdminLotes(admin.ModelAdmin):
	list_display = ('manzana','id','superficie','ocupado')
	list_filter = ('manzana', 'id', 'ocupado')