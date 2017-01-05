# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0024_auto_20170105_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='cantidad',
            field=models.DecimalField(max_digits=6, decimal_places=0, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
