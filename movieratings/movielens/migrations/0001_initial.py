# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genres', models.CharField(max_length=30)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('imbdid', models.IntegerField()),
                ('tmdbid', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('movieid', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('mpaa', models.IntegerField()),
                ('year', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('genres', models.ForeignKey(to='movielens.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Rantings',
            fields=[
                ('userid', models.IntegerField()),
                ('rating', models.FloatField()),
                ('timestamp', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('movieid', models.ForeignKey(to='movielens.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag', models.CharField(max_length=35)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('movieid', models.ForeignKey(to='movielens.Movies')),
                ('userid', models.ForeignKey(to='movielens.Rantings')),
            ],
        ),
        migrations.AddField(
            model_name='links',
            name='movieid',
            field=models.ForeignKey(to='movielens.Movies'),
        ),
    ]
