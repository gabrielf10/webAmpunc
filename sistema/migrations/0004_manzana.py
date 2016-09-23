# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20160923_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manzana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('proyecto', models.ForeignKey(to='sistema.Proyecto')),
            ],
        ),
    ]
