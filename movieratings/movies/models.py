from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Actors(models.Model):
    id = models.AutoField(primary_key=True)
    movie_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    character_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Links(models.Model):
    id = models.AutoField(primary_key=True)
    imdbid = models.IntegerField(default=0)
    tmdbid = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class movie(models.Model):
    movieid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Ratings(models.Model):
    userid = models.AutoField(primary_key=True)
    movieid = models.CharField(max_length=50)
    rating = models.FloatField(default=0)
    timestamp = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    userid = models.AutoField(primary_key=True)
    movieid = models.ForeignKey(movie)
    tag = models.CharField(max_length=200)
    timestamp = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
