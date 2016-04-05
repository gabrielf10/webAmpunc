# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0016_auto_20160229_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_izq',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'Descripci\xc3\xb3n Izquierda'),
        ),
    ]
