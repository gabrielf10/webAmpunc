# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_auto_20150808_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesSlide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('url', models.ImageField(upload_to=b'img', verbose_name=b'Im\xc3\xa1gen')),
            ],
            options={
                'verbose_name_plural': 'Imagenes Slide Portada',
            },
        ),
    ]
