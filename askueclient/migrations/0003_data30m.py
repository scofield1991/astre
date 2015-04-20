# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0002_delete_data30m'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data30M',
            fields=[
            ],
            options={
                'db_table': 'data_30m',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
