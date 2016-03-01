# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0014_auto_20160229_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_der',
            field=ckeditor.fields.RichTextField(verbose_name=b'Descripcion Derecha'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_izq',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
