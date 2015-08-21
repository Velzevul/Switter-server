# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 21, 17, 5, 10, 787048, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='log',
            name='participant_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
