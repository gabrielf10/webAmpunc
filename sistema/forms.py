from django import forms
from django.forms.formsets import formset_factory


class ProductForm(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
    price = forms.IntegerField()

ProductFormset= formset_factory(ProductForm)

class DistributorForm(forms.Form):
   name= forms.CharField()
   products= ProductFormset()