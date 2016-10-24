#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from sistema import views

urlpatterns = [
	url(r'^$', views.sistema_inicio, name='sistema'),
    url(r'^socios/$', views.sistema_socio, name='socio'),
    #url(r'^socio/(?P<slug>[-_\w]+)/$', 'sistema_socio', name="sistema_socio"),
]
