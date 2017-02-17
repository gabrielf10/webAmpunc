from .models import Socio
from django import forms
from django.forms.formsets import formset_factory

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'apellido': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'direccion': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'telefono': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'email': forms.TextInput(attrs={'class': 'myfieldclass'}),
            'fecha_ingreso': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }

nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	slug = models.SlugField(
	max_length=60, blank=True, null=True, editable=False)	
	direccion = models.CharField(max_length=255)
	telefono = models.PositiveIntegerField(unique=True)
	email = models.EmailField(max_length=255)
	fecha_ingreso = models.DateField()


class ProductForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
    price = forms.IntegerField()

ProductFormset= formset_factory(ProductForm)

class DistributorForm(forms.Form):
   name= forms.CharField()
   products= ProductFormset()