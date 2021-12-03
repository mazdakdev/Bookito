from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import *
from knox.models import AuthToken
import json
from PIL import Image
import tempfile


def Login(self):
    user = User.objects.create_superuser("admin" , "password")
    self.client.force_authenticate(user)
    response = self.client.get(reverse("user"))
    token = AuthToken.objects.create(user)
    self.client.credentials(Authorization=f'Token {token}')
    self.assertEqual(response.status_code, status.HTTP_200_OK)


#Function to create a test image
def img():
    image = Image.new('RGB' , (100,100))
    tmp_img = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(tmp_img)
    tmp_img.seek(0)
    return tmp_img
class CreateBookTestCase(APITestCase):
    def test_create_book(self):
        Login(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':'test' ,'category':'cat'  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        
        
class SearchBookTestCase(APITestCase):
    def test_search_book(self):
        Login(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':'test' ,'category':'cat'  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        response = self.client.get(reverse("search.book")+'?name=Booktest')
        print(response.content)
        name = json.loads(response.content)[0]["title"]
        self.assertEqual(name ,"Booktest" )
class ReadBooksTestCase(APITestCase):
    def test_read_books(self):
        Login(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':'test' ,'category':'cat'  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        response = self.client.get(reverse("read.book"))
        name = json.loads(response.content)[0]["title"]
        self.assertEqual( name , "Booktest" )

class UpdateBookTestCase(APITestCase):
    def test_update_books(self):
        Login(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':'test' ,'category':'cat'  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        tmp_edited_img = img()
        response = self.client.put(reverse('update.book' , kwargs={"id" : 1}) ,  {'title':'Booktestedited' , 'image':tmp_edited_img , 'author':'test' ,'category':'cat'  , 'user_id':1} , format="multipart")
        title = json.loads(response.content)["title"]
        self.assertEqual(title , "Booktestedited")

class DeleteBookTestCase(APITestCase):
    def test_delete_book(self):
        Login(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':'test' ,'category':'cat'  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        response = self.client.delete(reverse("delete.book" , kwargs={"id" : 1}))
        self.assertEqual(response.status_code , status.HTTP_200_OK)

class CreateInvalidBookTestCase(APITestCase):
    def test_create_invalid_book(self):
        Login(self)
        response = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':"test" , 'author':'test' ,'category':'cat'  , 'user_id':1} , format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)