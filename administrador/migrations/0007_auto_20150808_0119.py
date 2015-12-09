# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_auto_20150807_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproyecto',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name=b'Nombre'),
        ),
    ]
