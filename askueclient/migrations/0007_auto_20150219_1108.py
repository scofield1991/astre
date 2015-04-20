# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0006_auto_20150219_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='name',
            field=models.CharField(max_length=80),
            preserve_default=True,
        ),
    ]
