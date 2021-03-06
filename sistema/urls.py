#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from sistema import views

urlpatterns = [
	url(r'^$', views.sistema_inicio, name='sistema'),
    url(r'^socios/$', views.sistema_socio, name='socio'),
	url(r'^socios/(?P<slug>[-_\w]+)/$', views.sistema_socio_slug, name="socio-slug"),
	url(r'^socios/crear$', views.CrearSocioView.as_view(), name="crear_socio"),
	url(r'^socios/editar/(?P<pk>\d+)/$', views.EditarSocioView.as_view(), name="editar_socio"),
	url(r'^socios/eliminar/(?P<pk>\d+)/$', views.EliminarSocioView.as_view(), name="eliminar_socio"),
	url(r'^socios/pdf$', views.pdf, name="pdf"),
	url(r'^facturacion/$', views.sistema_facturacion, name='facturacion'),

    #url(r'^socio/(?P<slug>[-_\w]+)/$', 'sistema_socio', name="sistema_socio"),
]
