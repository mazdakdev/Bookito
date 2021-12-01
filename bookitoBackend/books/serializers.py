from django.db.models import fields
from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from .models import Book , Category , Author
from User.serializers import UserSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","title")

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ("id","name")

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ("id" , "title" , "image" , "author" , "category" , "pdf"  , "user_id" )