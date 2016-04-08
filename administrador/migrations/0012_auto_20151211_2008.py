# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_auto_20151113_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenesslide',
            name='url',
            field=models.ImageField(upload_to='img', verbose_name='Imágen'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_der',
            field=models.TextField(verbose_name='Descripcion Derecha'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_izq',
            field=models.TextField(verbose_name='Descripcion Izquierda'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='url',
            field=models.ImageField(upload_to='img', verbose_name='Imágen'),
        ),
    ]
