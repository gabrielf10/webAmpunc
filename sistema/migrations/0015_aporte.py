# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0014_auto_20161024_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('num_factura', models.PositiveIntegerField()),
                ('total', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('servicio', models.ForeignKey(to='sistema.Servicio')),
                ('socio', models.ForeignKey(to='sistema.Socio')),
            ],
        ),
    ]
