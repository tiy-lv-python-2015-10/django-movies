# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviekiller', '0004_rating_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='imdbid',
            new_name='imdb_id',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='movieid',
            new_name='movie_id',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='tmdbid',
            new_name='tmdb_id',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='movieid',
            new_name='movie_id',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='userid',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='movieid',
            new_name='movie_id',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='userid',
            new_name='user_id',
        ),
    ]
