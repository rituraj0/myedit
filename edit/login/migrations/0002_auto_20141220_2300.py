# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notepad',
            options={'get_latest_by': 'created'},
        ),
        migrations.AddField(
            model_name='notepad',
            name='author',
            field=models.CharField(max_length=50, default='admin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notepad',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
