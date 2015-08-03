# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_remove_tweet_retweet_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='retweet_authors',
        ),
        migrations.AddField(
            model_name='tweet',
            name='retweeted_by',
            field=models.ManyToManyField(related_name='retweeted_by', to='tweets.Author'),
        ),
    ]
