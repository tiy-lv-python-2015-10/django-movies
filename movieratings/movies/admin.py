from django.contrib import admin
from movies.models import movie
from movies.models import Actors
from movies.models import Ratings
from movies.models import Links
from movies.models import Tags

# Register your models here.
@admin.register(movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('movieid', 'title', 'genres', 'posted_at', 'modified_at')

@admin.register(Actors)
class actors(admin.ModelAdmin):
    list_display = ('id','name','character_name','dob')

@admin.register(Ratings)
class ratings(admin.ModelAdmin):
    list_display = ('userid',  'rating')

@admin.register(Links)
class links(admin.ModelAdmin):
    list_display = ('imdbid', 'tmdbid')

@admin.register(Tags)
class tags(admin.ModelAdmin):
    list_display = ('tag', 'timestamp')


