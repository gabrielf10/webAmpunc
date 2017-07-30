# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0026_auto_20170105_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallefactura',
            old_name='subtotal',
            new_name='valor',
        ),
    ]
