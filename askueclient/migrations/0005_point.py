# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askueclient', '0004_auto_20150213_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('obj', models.IntegerField()),
                ('name', models.CharField(unique=True, max_length=80)),
                ('klass_u', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
