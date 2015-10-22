# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20151021_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='actors',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('character_name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('movie_id', models.ForeignKey(to='movies.movie')),
            ],
        ),
    ]
