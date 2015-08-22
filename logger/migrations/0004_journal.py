# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20150821_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('participant_id', models.CharField(max_length=255)),
                ('created_at', models.CharField(default='***', max_length=255)),
                ('interesting_tweets_found', models.CharField(max_length=255)),
                ('interesting_tweets_description', models.CharField(max_length=255)),
                ('new_things_learnt', models.CharField(max_length=255)),
                ('new_things_description', models.CharField(max_length=255)),
                ('free_form_feedback', models.CharField(max_length=255, blank=True)),
            ],
        ),
    ]
