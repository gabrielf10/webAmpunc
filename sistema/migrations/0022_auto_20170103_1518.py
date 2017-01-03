# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sistema.models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0021_auto_20161106_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='num_factura',
            field=models.CharField(default=sistema.models.increment_numero_factura, max_length=500, null=True, blank=True),
        ),
    ]
