from django.contrib import admin
from moviekiller.models import Movie, Rating, Tag, Genre, Link

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'genres']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    fields = ['userid', 'movieid', 'rating', 'timestamp']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['userid', 'movieid', 'tag', 'timestamp']

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    fields = ['movieid', 'imdbid', 'tmdbid']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ['genre', 'id']
