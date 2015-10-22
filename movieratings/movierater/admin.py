from django.contrib import admin
from movierater.models import Movies, Links, Ratings, Tags, Genre


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'genres')

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('imdbid', 'tmdbid')

@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ('userid', 'movieid', 'rating', 'timestamp')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('userid', 'movieid', 'tag', 'timestamp')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    display = 'genres'