# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('screen_name', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('profile_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('favorite_count', models.IntegerField(null=True)),
                ('retweet_count', models.IntegerField(null=True)),
                ('text', models.CharField(null=True, default='', max_length=255)),
                ('author', models.ForeignKey(to='tweets.Author', db_column='author_screen_name')),
                ('original_tweet', models.ForeignKey(to='tweets.Tweet', null=True)),
                ('retweet_authors', models.ManyToManyField(to='tweets.Author', related_name='retweet_authors')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
