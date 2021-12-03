from django.db.models import fields
from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from .models import Book 
from User.serializers import UserSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ("id" , "title" , "image" , "author" , "category" , "pdf"  , "user_id" , "created_at" , "updated_at" )