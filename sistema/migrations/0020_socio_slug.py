# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0019_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 10, 27, 0, 6, 31, 418087, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
