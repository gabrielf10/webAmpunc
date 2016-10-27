# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0017_auto_20161024_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('importe', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
        ),
        migrations.RemoveField(
            model_name='factura',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='servicio',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(to='sistema.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='servicio',
            field=models.ForeignKey(to='sistema.Servicio'),
        ),
    ]
