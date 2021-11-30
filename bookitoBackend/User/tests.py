
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import *


# Class to test registration method
class CreateUserTestCase(APITestCase):
    def test_regestration(self):
        data = {"username" : "testcase" , "password" : "pass" ,
                 "first_name":"test case fname" , "last_name":"test case lname"}
        url = reverse("register")
        response = self.client.post(url , data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class LoginUserTestCase(APITestCase):
    def test_login(self):
        user = User.objects.create_user(username="test" , password="test")
        self.client.force_authenticate(user)
        response = self.client.get(reverse("user"))
        self.assertEqual(response.status_code , status.HTTP_200_OK)


