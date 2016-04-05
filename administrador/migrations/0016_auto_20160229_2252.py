# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0015_auto_20160229_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_der',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'Descripci\xc3\xb3n Derecha'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_izq',
            field=ckeditor.fields.RichTextField(verbose_name=b'Descripci\xc3\xb3n Izquierda'),
        ),
    ]
