# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_auto_20160923_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('valor_m2_terreno', models.DecimalField(max_digits=7, decimal_places=2)),
                ('valor_m2_urbanizacion', models.DecimalField(max_digits=7, decimal_places=2)),
                ('fecha_inicio', models.DateField()),
                ('actualizacion', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='zona',
            field=models.ForeignKey(to='sistema.Zona'),
        ),
    ]
