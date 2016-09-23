# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_auto_20160923_0620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manzana',
            options={'ordering': ('id',)},
        ),
        migrations.RemoveField(
            model_name='lote',
            name='numero',
        ),
    ]
