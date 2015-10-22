# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviekiller', '0002_auto_20151022_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='movieid',
            field=models.IntegerField(null=True),
        ),
    ]
