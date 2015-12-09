# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_imagenproyecto_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'verbose_name_plural': 'Proyectos'},
        ),
    ]
