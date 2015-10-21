# Django Movies

## Description

Django movies is an assignment to get an understanding of django with the 
[Movielens](http://grouplens.org/datasets/movielens/) dataset.

## Learning Objectives
* Create a new django project
* Create a new django app
* Create models in django
* Create a migration
* Run database migration

## Details

### Deliverables
* Django project with models and migrations
* Working admin with previously mentioned models

### Requirements
* No pep8 errors
* All packages in the requirements.txt

## Normal Mode
Create a `movieratings` django project. 

Create a new application in the `movieratings` project

Create Django models to represent the data.  Make sure that the data has the 
appropriate data types.  For simplicity sake you may skip the genre_movies table and skip the many to many relationship between movie and genre.

Make sure each model has 2 additional fields to track the date added and the
date modified.

Create django admin pages for your models.

Use the Django admin to add at least 3 entries into the movies, links, and tags models.  Put all of the genres into the genre model.

## Hard Mode
Export the data from the postgres database using 0xDBE and import it into the
new system.

Using the django shell create User objects to represent the user ids in the 
ratings table. `python manage.py shell`


