# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20160923_0656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lote',
            options={'ordering': ('id',)},
        ),
    ]
