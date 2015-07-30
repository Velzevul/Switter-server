# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_original_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='original_tweet',
            field=models.ForeignKey(null=True, to='tweets.Tweet'),
        ),
    ]
