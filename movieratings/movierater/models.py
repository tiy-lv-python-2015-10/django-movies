from django.db import models
from django.forms import IntegerField, FloatField


class Movies(models.Model):
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Links(models.Model):
    imdbid = IntegerField
    tmdbid = IntegerField
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Ratings(models.Model):
    userid = IntegerField
    movieid = models.ForeignKey(Movies)
    rating = FloatField
    timestamp = IntegerField
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    userid = IntegerField
    movieid = models.ForeignKey(Movies)
    tag = models.CharField(max_length=255)
    timestamp = IntegerField
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    genres = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)