from administrador.models import Proyecto, ImagenesSlide
from django.contrib import admin
from imagekit.admin import AdminThumbnail

# Register your models here.
class ImagenAdmin(admin.ModelAdmin):
	list_filter = ['titulo']
	image = AdminThumbnail(image_field ='imagen_miniatura',)
	list_display = ('titulo','image')

class ImagenSlide(admin.ModelAdmin):
	list_filter = ['nombre']
	image = AdminThumbnail(image_field ='imagen_miniatura')
	list_display = ('nombre','image') 
	

admin.site.register(Proyecto, ImagenAdmin)
admin.site.register(ImagenesSlide, ImagenSlide)

