# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0007_auto_20150219_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeDay',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('number_3min', models.CharField(max_length=30, db_column='3min', blank=True)),
                ('number_5min', models.CharField(max_length=30, db_column='5min', blank=True)),
                ('number_30min', models.CharField(max_length=30, db_column='30min', blank=True)),
                ('number_1hour', models.CharField(max_length=30, db_column='1hour', blank=True)),
            ],
            options={
                'db_table': 'time_day',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Point_kp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', models.IntegerField()),
                ('kp', models.IntegerField()),
            ],
            options={
                'db_table': 'point_kp',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='data30m',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='point',
            options={'managed': False},
        ),
    ]
