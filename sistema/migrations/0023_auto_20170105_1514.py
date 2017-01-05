# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0022_auto_20170103_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallefactura',
            old_name='importe',
            new_name='total',
        ),
    ]
