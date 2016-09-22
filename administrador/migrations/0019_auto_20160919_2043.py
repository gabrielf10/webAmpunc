# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0018_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenesslide',
            name='url',
            field=models.ImageField(upload_to=b'img', verbose_name=b'Im\xc3\xa1gen'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_der',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'Descripci\xc3\xb3n Derecha'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_izq',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'Descripci\xc3\xb3n Izquierda'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='url',
            field=models.ImageField(upload_to=b'img', verbose_name=b'Im\xc3\xa1gen'),
        ),
    ]
