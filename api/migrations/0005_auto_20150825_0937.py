# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150818_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='menu_items',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='panelbar_items',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='toolbar_items',
            field=models.TextField(default=None, null=True),
        ),
    ]
