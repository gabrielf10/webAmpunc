# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_imagenesslide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='descripcion_der',
            field=models.TextField(default=datetime.datetime(2015, 11, 12, 12, 5, 20, 196300, tzinfo=utc), verbose_name=b'Descripcion Derecha'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='descripcion_izq',
            field=models.TextField(default=datetime.datetime(2015, 11, 12, 12, 5, 32, 516212, tzinfo=utc), verbose_name=b'Descripcion Izquierda'),
            preserve_default=False,
        ),
    ]
