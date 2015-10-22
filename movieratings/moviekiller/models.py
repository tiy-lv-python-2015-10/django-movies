from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Rating(models.Model):
    user_id = models.IntegerField()
    movie_id = models.ForeignKey(Movie)
    rating = models.FloatField()
    timestamp = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    tag = models.CharField(max_length=100)
    timestamp = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Link(models.Model):
    imdb_id = models.IntegerField()
    tmdb_id = models.IntegerField()
    movie_id = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)





