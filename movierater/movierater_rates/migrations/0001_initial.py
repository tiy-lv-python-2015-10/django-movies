# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('movieid', models.IntegerField()),
                ('imdbid', models.IntegerField()),
                ('tmdbid', models.IntegerField()),
                ('Add_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('movieid', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=100)),
                ('Add_date', models.DateTimeField()),
                ('modified_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('ratingid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('movieid', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('timestamp', models.DateTimeField()),
                ('Add_date', models.DateTimeField()),
                ('modified_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('userid', models.IntegerField()),
                ('movieid', models.IntegerField()),
                ('tag', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('Add_date', models.DateTimeField()),
                ('modified_date', models.DateTimeField()),
            ],
        ),
    ]
