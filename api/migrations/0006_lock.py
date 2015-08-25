# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150825_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
            ],
        ),
    ]
