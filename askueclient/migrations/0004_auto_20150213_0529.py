# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0003_data30m'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data30M',
        ),
        migrations.CreateModel(
            name='Data30M',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('dtime', models.DateTimeField()),
                ('point', models.IntegerField()),
                ('param', models.IntegerField()),
                ('zn', models.FloatField()),
            ],
            options={
                'db_table': 'data_30m',
            },
            bases=(models.Model,),
        ),
    ]
