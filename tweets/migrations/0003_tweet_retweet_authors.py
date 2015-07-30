# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_tweet_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='retweet_authors',
            field=models.ManyToManyField(related_name='retweet_authors', to='tweets.Author'),
        ),
    ]
