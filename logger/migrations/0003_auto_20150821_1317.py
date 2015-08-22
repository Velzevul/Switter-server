# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_auto_20150821_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='created_at',
            field=models.CharField(max_length=255, default='***'),
        ),
    ]
