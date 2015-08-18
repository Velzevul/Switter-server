# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150818_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={},
        ),
        migrations.AddField(
            model_name='tweet',
            name='is_deployed',
            field=models.BooleanField(default=False),
        ),
    ]
