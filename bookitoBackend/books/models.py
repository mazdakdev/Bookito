from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=20)

class Author(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField()
    price = models.CharField(max_length=20)
    author = models.ForeignKey(Author, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)
    description = models.TextField()


    