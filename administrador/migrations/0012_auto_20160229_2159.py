# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_auto_20151113_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_der',
            field=ckeditor.fields.RichTextField(help_text='Redacta una descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_izq',
            field=ckeditor.fields.RichTextField(help_text='Redacta una descripci\xf3n'),
        ),
    ]
