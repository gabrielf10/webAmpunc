# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_auto_20150807_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproyecto',
            name='url',
            field=models.ImageField(upload_to=b'img', verbose_name=b'Im\xc3\xa1gen'),
        ),
    ]
