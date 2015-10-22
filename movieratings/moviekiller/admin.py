from django.contrib import admin
from moviekiller.models import Movie, Rating, Tag, Genre, Link

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genres']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'movie_id', 'rating', 'timestamp']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'movie_id', 'tag', 'timestamp']

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['movie_id', 'imdb_id', 'tmdb_id']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'id']
