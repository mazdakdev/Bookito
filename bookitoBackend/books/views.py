from django.shortcuts import render
from rest_framework import status
from .serializers import  *
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
       
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
       
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def get_authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors , many=True)
        return Response(serializer.data)
    return Response("Something Went Wrong" , status=status.HTTP_400_BAD_REQUEST)



@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def update_author(request , id):
    if request.method == 'PUT':
        author = Author.objects.get(id=id)
        serializer = AuthorSerializer(author , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        

@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def delete_author(request , id):
    if request.method == 'DELETE':
        author = Author.objects.get(id=id)
        author.delete()
        return Response("Deleted successfully ! " )


    
@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data , status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(["GET"])
def read_books(request):
    if request.method == "GET":
        books = Book.objects.filter(user_id = request.user.id)
        serializer = BookSerializer(books , many=True)
        return Response(serializer.data)
    return Response("Something Went Wrong" , status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def update_book(request , id):
    if request.method == 'PUT':
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        

@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def delete_book(request , id):
    if request.method == 'DELETE':
        book = Book.objects.get(id=id)
        book.delete()
        return Response("Deleted successfully ! " )

# Function to get book ordered by their category
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_books_by_category(request , id):
    if request.method == "GET":
        books = Book.objects.filter(category__id=id)
        serializer = BookSerializer(books , many=True)
        return Response(serializer.data)
    return Response("Some thing went wrong" , status=status.HTTP_400_BAD_REQUEST)
     

# Function to get book ordered by their Author
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_book_by_author(request , id):
    if request.method == "GET":
        books = Book.objects.filter(author__id=id)
        serializer = BookSerializer(books , Many=True)
        return Response(serializer.data)
    return Response("Some thing went wrong" , status=status.HTTP_400_BAD_REQUEST)

# Function's to get last 6 books Decending, ascending

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_lastest_updated_books(request):
    if request.method == "GET":
        last_six = Book.objects.filter(user_id=request.user.id).order_by('-id')[:10]
        last_six_in_ascending_order = reversed(last_six)
        serializer = BookSerializer(last_six_in_ascending_order , Many=True)
        return Response(serializer.data)
    return Response("Some thing went wrong" , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_latest_updated_books_descending(request):
    if request.method == "GET":
        last_six = Book.objects.filter(user_id=request.user.id).order_by('-id')[:10]
        serializer = BookSerializer(last_six , Many=True)
        return Response(serializer.data)
    return Response("Some thing went wrong" , status=status.HTTP_400_BAD_REQUEST)

