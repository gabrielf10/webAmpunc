# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0019_auto_20161027_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='socio',
            field=models.ForeignKey(blank=True, to='sistema.Socio', null=True),
        ),
    ]
