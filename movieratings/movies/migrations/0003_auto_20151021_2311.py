# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20151021_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 21, 23, 11, 21, 428387, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 21, 23, 11, 40, 123696, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
