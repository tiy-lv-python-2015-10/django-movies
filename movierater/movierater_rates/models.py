from django.db import models


class Links(models.Model):
    movieid = models.IntegerField()
    imdbid = models.IntegerField()
    tmdbid = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Genres(models.Model):
    genres = models.CharField(max_length=50)
    genreid = models.IntegerField(primary_key=True)


class Movies(models.Model):
    movieid = models.IntegerField()
    title = models.CharField(max_length=100)
    genreid = models.ForeignKey(Genres)
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Ratings(models.Model):
    ratingid = models.IntegerField()
    userid = models.IntegerField()
    movieid = models.ForeignKey(Movies)
    rating = models.DecimalField(decimal_places=2, max_digits=2)
    timestamp = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    userid = models.IntegerField()
    movieid = models.IntegerField()
    tag = models.CharField(max_length=100)
    timestamp = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
