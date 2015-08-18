# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150804_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='menu_items',
            field=models.CharField(null=True, max_length=255, default=None),
        ),
        migrations.AddField(
            model_name='tweet',
            name='panelbar_items',
            field=models.CharField(null=True, max_length=255, default=None),
        ),
        migrations.AddField(
            model_name='tweet',
            name='preview_image_url',
            field=models.CharField(null=True, max_length=255, default=None),
        ),
        migrations.AddField(
            model_name='tweet',
            name='toolbar_items',
            field=models.CharField(null=True, max_length=255, default=None),
        ),
    ]
