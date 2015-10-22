from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Links(models.Model):
    imdbid = models.IntegerField(default=0)
    tmdbid = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Ratings(models.Model):
    userid = models.IntegerField(default=0)
    movieid = models.ForeignKey(Movies)
    rating = models.FloatField(default=0)
    timestamp = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    userid = models.IntegerField(default=0)
    movieid = models.ForeignKey(Movies)
    tag = models.CharField(max_length=255)
    timestamp = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    genres = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)