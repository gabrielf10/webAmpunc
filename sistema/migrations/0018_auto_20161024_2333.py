# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0017_auto_20161024_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='servicio',
        ),
        migrations.AddField(
            model_name='servicio',
            name='factura',
            field=models.ForeignKey(default=12, to='sistema.Factura'),
            preserve_default=False,
        ),
    ]
