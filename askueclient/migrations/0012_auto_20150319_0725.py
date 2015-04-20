# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0011_auto_20150319_0704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data1h',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='point_kp',
            options={'managed': False},
        ),
    ]
