from django.shortcuts import render
from rest_framework import status
from .serializers import  *
from .models import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User


    
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
        book = Book.objects.get(id=id , user_id=request.user.id)
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

# Function's to get last 4 books Decending, ascending

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_lastest_updated_books(request):
    if request.method == "GET":
        last_four = Book.objects.filter(user_id=request.user.id).order_by('-id')[:4]
        last_fpur_in_ascending_order = reversed(last_six)
        serializer = BookSerializer(last_four , Many=True)
        return Response(serializer.data)
    return Response("Some thing went wrong" , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_latest_updated_books_descending(request):
    if request.method == "GET":
        last_four = Book.objects.filter(user_id=request.user.id).order_by('-id')[:4]
        serializer = BookSerializer(last_four , Many=True)
        return Response(serializer.data)
    return Response("Some thing went wrong" , status=status.HTTP_400_BAD_REQUEST)

@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def Search_books(request ):
    if request.method == 'GET':
        get_data = request.query_params.get('name')
        books = Book.objects.filter(title=get_data , user_id=request.user.id)
        serializer = BookSerializer(books , many=True)
        return Response(serializer.data)
    return Response("Some thing went wrong" , status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([permissions.IsAuthenticated])
@api_view(["GET"])
def get_book_by_id(request , id):
    if request.method == "GET":
        book = Book.objects.get(user_id = request.user.id , id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    return Response("Something Went Wrong" , status=status.HTTP_400_BAD_REQUEST)
