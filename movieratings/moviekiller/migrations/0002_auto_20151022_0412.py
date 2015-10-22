# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviekiller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('rating', models.FloatField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='movieid',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='movieid',
            field=models.ForeignKey(to='moviekiller.Movie'),
        ),
    ]
