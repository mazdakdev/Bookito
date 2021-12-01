from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=20)

class Author(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField()
    pdf = models.FileField(upload_to ='pdf/% Y/% m/% d/',blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    