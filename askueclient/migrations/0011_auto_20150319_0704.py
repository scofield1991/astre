# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0010_groups'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='groups',
            table='groups',
        ),
    ]
