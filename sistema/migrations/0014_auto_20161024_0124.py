# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0013_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='interes',
            field=models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
