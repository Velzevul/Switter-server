# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0004_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='free_form_feedback',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='interesting_tweets_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='journal',
            name='new_things_description',
            field=models.TextField(),
        ),
    ]
