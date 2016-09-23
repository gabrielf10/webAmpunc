# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_auto_20160923_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='valor_m2_terreno',
            field=models.DecimalField(max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='valor_m2_urbanizacion',
            field=models.DecimalField(max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
