# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0010_deuda_sociodeuda'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='socio',
            field=models.ForeignKey(default=1, to='sistema.Socio'),
            preserve_default=False,
        ),
    ]
