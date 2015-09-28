# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('city', models.CharField(max_length=100)),
                ('state_long', models.CharField(max_length=100)),
                ('state_short', models.CharField(max_length=2)),
            ],
        ),
    ]
