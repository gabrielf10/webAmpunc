# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0025_auto_20170105_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='descripcion',
            field=models.CharField(default='probando', help_text=b'Descripci\xc3\xb3n del servicio.', max_length=100, verbose_name=b'Descripci\xc3\xb3n'),
            preserve_default=False,
        ),
    ]
