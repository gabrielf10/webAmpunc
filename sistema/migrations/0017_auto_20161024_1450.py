# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0016_auto_20161024_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_factura', models.PositiveIntegerField(unique=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('interes', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('servicio', models.ForeignKey(to='sistema.Servicio')),
                ('socio', models.ForeignKey(to='sistema.Socio')),
            ],
        ),
        migrations.RemoveField(
            model_name='aporte',
            name='servicio',
        ),
        migrations.RemoveField(
            model_name='aporte',
            name='socio',
        ),
        migrations.DeleteModel(
            name='Aporte',
        ),
    ]
