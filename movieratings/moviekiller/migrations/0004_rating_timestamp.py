# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviekiller', '0003_link_movieid'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.IntegerField(null=True),
        ),
    ]
