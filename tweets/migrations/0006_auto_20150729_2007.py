# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20150729_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='favorite_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweet_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=255, default='', null=True),
        ),
    ]
