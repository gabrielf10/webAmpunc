# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_imagenproyecto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproyecto',
            name='url',
            field=models.ImageField(upload_to=b'static/img', verbose_name=b'Im\xc3\xa1gen'),
        ),
    ]
