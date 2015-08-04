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
                ('screen_name', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('profile_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('created_at', models.DateTimeField()),
                ('favorite_count', models.IntegerField(null=True)),
                ('text', models.CharField(default='', null=True, max_length=255)),
                ('author', models.ForeignKey(db_column='author_screen_name', to='api.Author')),
                ('original_tweet', models.ForeignKey(null=True, to='api.Tweet')),
                ('retweeted_by', models.ManyToManyField(null=True, related_name='retweeted_by', to='api.Author')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
