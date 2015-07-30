# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_tweet_retweet_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='original_tweet',
            field=models.ForeignKey(to='tweets.Tweet'),
        ),
    ]
