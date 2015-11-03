from django.contrib import admin
from movierater_rates.models import Links, Genres, Movies, Ratings, Tags

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('movieid', 'imdbid',
                    'tmdbid', 'add_date',
                    'modified_date')

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('genres', 'genreid')

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('movieid', 'title',
                    'genreid', 'add_date',
                    'modified_date')

@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('ratingid', 'userid',
                    'movieid', 'rating',
                    'timestamp', 'add_date',
                    'modified_date')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('userid', 'movieid',
                    'tag', 'timestamp',
                    'add_date', 'modified_date')