from django.db import models


class Links(models.Model):
    movieid = models.IntegerField()
    imdbid = models.IntegerField()
    tmdbid = models.IntegerField()
    Add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Movies(models.Model):
    movieid = models.IntegerField()
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    Add_date = models.DateTimeField()
    modified_date = models.DateTimeField()


class Ratings(models.Model):
    ratingid = models.IntegerField()
    userid = models.IntegerField()
    movieid = models.IntegerField()
    rating = models.DecimalField(decimal_places=2, max_digits=2)
    timestamp = models.DateTimeField()
    Add_date = models.DateTimeField()
    modified_date = models.DateTimeField()


class Tags(models.Model):
    userid = models.IntegerField()
    movieid = models.IntegerField()
    tag = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    Add_date = models.DateTimeField()
    modified_date = models.DateTimeField()
