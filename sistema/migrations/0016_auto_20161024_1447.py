# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0015_aporte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aporte',
            old_name='total',
            new_name='interes',
        ),
        migrations.RenameField(
            model_name='servicio',
            old_name='cextraordinaria',
            new_name='importe',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='csocial',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='cterreno',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='curbanizacion',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='gadministrativos',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='interes',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='otros',
        ),
        migrations.AddField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(default=datetime.datetime(2016, 10, 24, 14, 47, 46, 843455, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aporte',
            name='num_factura',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.CharField(help_text=b'Descripci\xc3\xb3n del servicio.', max_length=100, verbose_name=b'Descripci\xc3\xb3n'),
        ),
    ]
