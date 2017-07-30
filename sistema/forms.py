#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .models import Socio
from django import forms
from django.forms.formsets import formset_factory
from django.forms.extras.widgets import SelectDateWidget


class SocioModelForm(forms.ModelForm):
    nombre = forms.CharField(label='', widget= forms.TextInput(
        attrs={
            "class": "txt_nombre",
            "placeholder": "Nombre del Socio",
        }))
    apellido = forms.CharField(label='',widget= forms.TextInput(
        attrs={
            "class": "txt_apellido",
            "placeholder": "Apellido del Socio",
        }))
    direccion = forms.CharField(label='',widget= forms.TextInput(
        attrs={
            "class": "txt_direccion",
            "placeholder": "Dirección del Socio",
        }))
    telefono = forms.CharField(label='',widget= forms.TextInput(
        attrs={
            "class": "txt_telefono",
            "placeholder": "Teléfono del Socio",
        }))
    email = forms.EmailField(label='',widget= forms.EmailInput(
        attrs={
            "class": "txt_email",
            "placeholder": "Email del Socio",
        }))
    
    

    class Meta:
        model = Socio
        fields = '__all__'
        widgets = {
        'fecha_ingreso': SelectDateWidget(),
    }
        

    



class ProductForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
    price = forms.IntegerField()

ProductFormset= formset_factory(ProductForm)

class DistributorForm(forms.Form):
   name= forms.CharField()
   products= ProductFormset()
