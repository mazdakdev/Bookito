from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField()
    pdf = models.FileField(upload_to ='pdf/',blank=True)
    author = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    