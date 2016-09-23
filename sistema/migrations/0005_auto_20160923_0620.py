# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_manzana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('superficie', models.DecimalField(max_digits=6, decimal_places=2)),
                ('ocupado', models.BooleanField(default=False)),
                ('manzana', models.ForeignKey(to='sistema.Manzana')),
            ],
        ),
        migrations.AlterField(
            model_name='socio',
            name='telefono',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
