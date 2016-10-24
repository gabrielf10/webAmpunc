# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sistema.models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0012_lote_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('csocial', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('gadministrativos', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('cextraordinaria', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('curbanizacion', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('cterreno', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('otros', models.DecimalField(max_digits=6, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('descripcion', models.CharField(help_text=b'Descripci\xc3\xb3n del campo otros.', max_length=100, verbose_name=b'Descripci\xc3\xb3n')),
                ('interes', models.DecimalField(max_digits=6, decimal_places=2, validators=[])),
            ],
        ),
    ]
