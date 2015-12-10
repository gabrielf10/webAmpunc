# -*- coding: utf-8 -*-
"""webAmpunc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
import os

admin.autodiscover()

admin.site.site_title = u'Adiministración Sitio Web AMPUNC'
admin.site.site_header = u'Adiministración Sitio Web AMPUNC'
admin.site.index_title = u'Panel de Control AMPUNC'

urlpatterns = [
    url(r'^$','administrador.views.inicio'),
    url(r'^contacto/', include('contact_form.urls')),
    url(r'^institucional/$', 'administrador.views.institucional'),
    url(r'^proyectos/$', 'administrador.views.proyectos'),
    url(r'^encuesta/$', 'administrador.views.encuesta'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT,'js')}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT,'css')}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT,'img')}),
]
