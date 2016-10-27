# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0020_socio_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='slug',
            field=models.SlugField(max_length=60, null=True, editable=False, blank=True),
        ),
    ]
