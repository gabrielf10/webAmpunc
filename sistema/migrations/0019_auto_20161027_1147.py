# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0018_auto_20161025_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='factura',
            field=models.ForeignKey(default=1, to='sistema.Factura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socio',
            name='slug',
            field=models.SlugField(max_length=60, null=True, editable=False, blank=True),
        ),
    ]
