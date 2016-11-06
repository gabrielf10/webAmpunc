# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0020_auto_20161030_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='interes',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='factura',
        ),
        migrations.AddField(
            model_name='factura',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2016, 11, 6, 16, 41, 12, 794296, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
