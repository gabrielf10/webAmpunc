# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_lote_socio'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='numero',
            field=models.CharField(default=datetime.datetime(2016, 10, 23, 17, 39, 32, 959234, tzinfo=utc), max_length=3),
            preserve_default=False,
        ),
    ]
