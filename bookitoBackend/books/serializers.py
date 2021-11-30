from django.db.models import fields
from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from .models import Book , Category , Author

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","title")

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ("id","name")

class Book(ModelSerializer):
    class Meta:
        model = Book
        fields = ("id" , "title" , "image", "price" , "author" , "category" , "description")