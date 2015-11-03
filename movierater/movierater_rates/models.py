from django.db import models


class Links(models.Model):
    movieid = models.IntegerField()
    imdbid = models.IntegerField()
    tmdbid = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Movie: {}, Imdbid: {}, Tmdbid: {}, Add_date: {}, Modified_date:{}".format(
            self.movieid, self.imdbid, self.tmdbid, self.add_date, self.modified_date)


class Genres(models.Model):
    genres = models.CharField(max_length=50)
    genreid = models.IntegerField(primary_key=True)
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Genres: {}, Genreid: {}, Add_date: {}, Modified_date: {}".format(
            self.genres, self.genreid, self.add_date, self.modified_date)


class Movies(models.Model):
    movieid = models.IntegerField()
    title = models.CharField(max_length=100)
    genreid = models.ForeignKey(Genres)
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Movieid: {}, Title: {}, Genreid: {}, Add_date: {}, Modified_date: {}".format(
            self.movieid, self.title, self.genreid, self.add_date, self.modified_date)


class Ratings(models.Model):
    ratingid = models.IntegerField()
    userid = models.IntegerField()
    movieid = models.ForeignKey(Movies)
    rating = models.DecimalField(decimal_places=2, max_digits=2)
    timestamp = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Ratingid: {}, Userid: {}, Movieid: {}, Rating: {}, Timestamp: {}, Add_date: {}, Modified_date: {}".\
            format(self.ratingid, self.userid, self.movieid, self.rating, self.timestamp, self.add_date,
                   self.modified_date)


class Tags(models.Model):
    userid = models.IntegerField()
    movieid = models.IntegerField()
    tag = models.CharField(max_length=100)
    timestamp = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "userid: {}, movieid: {}, tag: {}, timestamp: {}, add_date:{}, modified_date: {}".format(
            self.userid, self.movieid, self.tag, self.timestamp, self.add_date, self.modified_date)
