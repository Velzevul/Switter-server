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
                ('screen_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('profile_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('favorite_count', models.IntegerField()),
                ('retweet_count', models.IntegerField()),
                ('author', models.ForeignKey(db_column='author_screen_name', to='tweets.Author')),
            ],
        ),
    ]
