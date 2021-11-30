from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import *
from knox.models import AuthToken
import json


class CreateCategoryTestCase(APITestCase):
    def test_add_category(self):
        user = User.objects.create_superuser('admin', 'admin@example.com')
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        token = AuthToken.objects.create(user)

        self.client.credentials(Authorization=f'Token {token}')
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

class ReadCategoryTestCase(APITestCase):
    def test_read_category(self):
        user = User.objects.create_superuser('admin', 'admin@example.com')
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        token = AuthToken.objects.create(user)
        self.client.credentials(Authorization=f'Token {token}')
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

        response_ = self.client.get(reverse("read.category"))
        name = json.loads(response_.content)[0]["title"]
        self.assertEqual( name , "TestCat" )

class UpdateCategoryTestCase(APITestCase):
    def test_update_category(self):
        user = User.objects.create_superuser('admin', 'admin@example.com')
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        token = AuthToken.objects.create(user)
        self.client.credentials(Authorization=f'Token {token}')
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

        response_ = self.client.put(reverse("update.category" , kwargs={'id':1}) ,{'title':'TestCatEdited'} )
        title = json.loads(response_.content)["title"]
        self.assertEqual(title , "TestCatEdited" )


class DeleteCategoryTestCase(APITestCase):
    def test_delete_category(self):
        user = User.objects.create_superuser('admin', 'admin@example.com')
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        token = AuthToken.objects.create(user)
        self.client.credentials(Authorization=f'Token {token}')
        response_category = self.client.post(reverse("create.category") , {'title':'TestCat'})
        self.assertEqual(response_category.status_code , status.HTTP_201_CREATED)

        response_ = self.client.delete(reverse("delete.category" , kwargs={"id" : 1}))
        self.assertEqual(response_.status_code , status.HTTP_200_OK)


class CreateAuthorTestCase(APITestCase):
    def test_add_Author(self):
        user = User.objects.create_superuser('admin', 'admin@example.com')
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        token = AuthToken.objects.create(user)

        self.client.credentials(Authorization=f'Token {token}')
        response_author = self.client.post(reverse("create.author") , {'name':'TestAuthor'})
        self.assertEqual(response_author.status_code , status.HTTP_201_CREATED)




class UpdateAuthorTestCase(APITestCase):
    def test_update_Author(self):
        user = User.objects.create_superuser('admin', 'admin@example.com')
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        token = AuthToken.objects.create(user)
        self.client.credentials(Authorization=f'Token {token}')
        response_author = self.client.post(reverse("create.author") , {'name':'TestAuthor'})
        self.assertEqual(response_author.status_code , status.HTTP_201_CREATED)

        response_ = self.client.put(reverse("update.author" , kwargs={'id':1}) ,{'name':'TestAuthorEdited'} )
        name = json.loads(response_.content)["name"]
        self.assertEqual(name , "TestAuthorEdited" )



class DeleteAuthorTestCase(APITestCase):
    def test_delete_author(self):
        user = User.objects.create_superuser('admin', 'admin@example.com')
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))

        self.assertEqual(response.status_code , status.HTTP_200_OK)
        token = AuthToken.objects.create(user)
        self.client.credentials(Authorization=f'Token {token}')
        response_author = self.client.post(reverse("create.author") , {'name':'TestAuthor'})
        self.assertEqual(response_author.status_code , status.HTTP_201_CREATED)

        response_ = self.client.delete(reverse("delete.author" , kwargs={"id" : 1}))
        self.assertEqual(response_.status_code , status.HTTP_200_OK)

