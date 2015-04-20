# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0008_auto_20150306_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data1H',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtime', models.DateTimeField()),
                ('point', models.IntegerField()),
                ('param', models.IntegerField()),
                ('zn', models.FloatField()),
            ],
            options={
                'db_table': 'data_1h',
            },
            bases=(models.Model,),
        ),
    ]
