# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0009_auto_20160923_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deuda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('importe', models.DecimalField(max_digits=7, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
        ),
        migrations.CreateModel(
            name='SocioDeuda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('deuda', models.ForeignKey(to='sistema.Deuda')),
                ('socio', models.ForeignKey(to='sistema.Socio')),
            ],
        ),
    ]
