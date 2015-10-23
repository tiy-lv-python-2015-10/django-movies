from django.db import models


class Genre(models.Model):
    genres = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Movies(models.Model):
    movieid = models.IntegerField()
    title = models.CharField(max_length=255)
    genres = models.ForeignKey(Genre)
    mpaa = models.CharField(max_length=5)
    year = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Rantings(models.Model):
    userid = models.IntegerField()
    movieid = models.ForeignKey(Movies)
    rating = models.FloatField()
    timestamp = models.IntegerField()
    id = models.AutoField(primary_key=True)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Links(models.Model):
    movieid = models.ForeignKey(Movies)
    imbdid = models.IntegerField()
    tmdbid = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    userid = models.ForeignKey(Rantings)
    movieid = models.ForeignKey(Movies)
    tag = models.CharField(max_length=35)
    id = models.AutoField(primary_key=True)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
