# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20150803_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='retweeted_by',
            field=models.ManyToManyField(related_name='retweeted_by', null=True, to='tweets.Author'),
        ),
    ]
