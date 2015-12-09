# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0009_auto_20151112_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='url',
            field=models.ImageField(default=datetime.datetime(2015, 11, 13, 15, 55, 52, 456764, tzinfo=utc), upload_to=b'img', verbose_name=b'Im\xc3\xa1gen'),
            preserve_default=False,
        ),
    ]
