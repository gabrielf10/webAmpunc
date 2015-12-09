# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenProyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Im\xe1genes',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='imagenproyecto',
            name='proyecto',
            field=models.ForeignKey(verbose_name=b'Proyecto', to='administrador.Proyecto'),
        ),
    ]
