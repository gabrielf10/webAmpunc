# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenproyecto',
            name='url',
            field=models.ImageField(default=datetime.datetime(2015, 8, 6, 19, 16, 8, 405646, tzinfo=utc), upload_to=b'img', verbose_name=b'Im\xc3\xa1gen'),
            preserve_default=False,
        ),
    ]
