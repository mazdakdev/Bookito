from django.shortcuts import render
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User


#Function to create Category

@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def create_category(request):
    if request.method == 'POST':
        if request.user.has_perm("books.add_category"):
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response("Sorry but you don't have permission to do this" , status=status.HTTP_403_FORBIDDEN )
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#Function to Retrieve Categories

@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def get_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories , many=True)
        return Response(serializer.data)
    return Response("Something Went Wrong" , status=status.HTTP_400_BAD_REQUEST)


#Function to update Category

@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def update_category(request , id):
    if request.method == 'PUT':
        if request.user.has_perm("books.update_category"):
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category,request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response("Sorry but you don't have permission to do this" , status=status.HTTP_403_FORBIDDEN )

        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
#Function to delete category

@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def delete_category(request , id):
    if request.method == 'DELETE':
        if request.user.has_perm("books.delete_category"):
            category = Category.objects.get(id=id)
            category.delete()
            return Response("Deleted successfully ! ")
        else:
            return Response("Sorry but you don't have permission to do this" , status=status.HTTP_403_FORBIDDEN )



@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def create_author(request):
    if request.method == 'POST':
        if request.user.has_perm("books.add_author"):
            serializer = AuthorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response("Sorry but you don't have permission to do this" , status=status.HTTP_403_FORBIDDEN )
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def get_authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = CategorySerializer(authors , many=True)
        return Response(serializer.data)
    return Response("Something Went Wrong" , status=status.HTTP_400_BAD_REQUEST)



@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def update_author(request , id):
    if request.method == 'PUT':
        if request.user.has_perm("books.update_author"):
            author = Author.objects.get(id=id)
            serializer = AuthorSerializer(author , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response("Sorry but you don't have permission to do this" , status=status.HTTP_403_FORBIDDEN )
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        

@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def delete_author(request , id):
    if request.method == 'DELETE':
        if request.user.has_perm("books.delete_author"):
            author = Author.objects.get(id=id)
            Author.delete()
            return Response("Deleted successfully ! " )
        else:
            return Response("Sorry but you don't have permission to do this" , status=status.HTTP_403_FORBIDDEN )


    

