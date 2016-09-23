# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
