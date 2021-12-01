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

class CreateCategoryTestCase(APITestCase):
    def test_add_category(self):
        Login(self)
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

class ReadCategoryTestCase(APITestCase):
    def test_read_category(self):
        Login(self) 
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

        response_ = self.client.get(reverse("read.category"))
        name = json.loads(response_.content)[0]["title"]
        self.assertEqual( name , "TestCat" )

class UpdateCategoryTestCase(APITestCase):
    def test_update_category(self):
        Login(self)
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

        response_ = self.client.put(reverse("update.category" , kwargs={'id':1}) ,{'title':'TestCatEdited'} )
        title = json.loads(response_.content)["title"]
        self.assertEqual(title , "TestCatEdited" )


class DeleteCategoryTestCase(APITestCase):
    def test_delete_category(self):
        Login(self)
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

        response_ = self.client.delete(reverse("delete.category" , kwargs={"id" : 1}))
        self.assertEqual(response_.status_code , status.HTTP_200_OK)


class CreateAuthorTestCase(APITestCase):
    def test_add_Author(self):
        Login(self) 
        response_author = self.client.post(reverse("create.author") , {'name':'TestAuthor'})
        self.assertEqual(response_author.status_code , status.HTTP_201_CREATED)




class UpdateAuthorTestCase(APITestCase):
    def test_update_Author(self):
        Login(self)
        response_author = self.client.post(reverse("create.author") , {'name':'TestAuthor'})
        self.assertEqual(response_author.status_code , status.HTTP_201_CREATED)

        response_ = self.client.put(reverse("update.author" , kwargs={'id':1}) ,{'name':'TestAuthorEdited'} )
        name = json.loads(response_.content)["name"]
        self.assertEqual(name , "TestAuthorEdited" )



class DeleteAuthorTestCase(APITestCase):
    def test_delete_author(self):
        Login(self)
        response_author = self.client.post(reverse("create.author") , {'name':'TestAuthor'})
        self.assertEqual(response_author.status_code , status.HTTP_201_CREATED)

        response_ = self.client.delete(reverse("delete.author" , kwargs={"id" : 1}))
        self.assertEqual(response_.status_code , status.HTTP_200_OK)

def Createreq(self):
    Login(self)
    response_author = self.client.post(reverse("create.author") , {'name':'TestAuthor'})
    self.assertEqual(response_author.status_code , status.HTTP_201_CREATED)
    response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
    self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)


#Function to create a test image
def img():
    image = Image.new('RGB' , (100,100))
    tmp_img = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(tmp_img)
    tmp_img.seek(0)
    return tmp_img
class CreateBookTestCase(APITestCase):
    def test_create_book(self):
        Createreq(self)

        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':1 ,'category':1  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        
        
class ReadBooksTestCase(APITestCase):
    def test_read_books(self):
        Createreq(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':1 ,'category':1  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        response = self.client.get(reverse("read.book"))
        name = json.loads(response.content)[0]["title"]
        self.assertEqual( name , "Booktest" )

class UpdateBookTestCase(APITestCase):
    def test_update_books(self):
        Createreq(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':1 ,'category':1  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        tmp_edited_img = img()
        response = self.client.put(reverse('update.book' , kwargs={"id" : 1}) ,  {'title':'Booktestedited' , 'image':tmp_edited_img , 'author':1 ,'category':1  , 'user_id':1} , format="multipart")
        title = json.loads(response.content)["title"]
        self.assertEqual(title , "Booktestedited")

class DeleteBookTestCase(APITestCase):
    def test_delete_book(self):
        Createreq(self)
        tmp_img = img()
        response_book = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':tmp_img , 'author':1 ,'category':1  , 'user_id':1} , format="multipart")
        self.assertEqual(response_book.status_code , status.HTTP_201_CREATED)
        response = self.client.delete(reverse("delete.book" , kwargs={"id" : 1}))
        self.assertEqual(response.status_code , status.HTTP_200_OK)

class CreateInvalidBookTestCase(APITestCase):
    def test_create_invalid_book(self):
        Createreq(self)
        response = self.client.post(reverse("create.book") , {'title':'Booktest' , 'image':"test" , 'author':1 ,'category':1  , 'user_id':1} , format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)