# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_actors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imdbid', models.IntegerField(default=0)),
                ('tmdbid', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('movieid', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0)),
                ('timestamp', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=200)),
                ('timestamp', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('movieid', models.ForeignKey(to='movies.movie')),
            ],
        ),
        migrations.AlterField(
            model_name='actors',
            name='movie_id',
            field=models.CharField(max_length=50),
        ),
    ]
