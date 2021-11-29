from django.urls import path
from .api import *
from knox import views as knox_views

urlpatterns = [

    #domain.dn/api/v1/register/ | POST
    path('register/' , SignUpAPI.as_view() , name='register'),

    #domain.dn/api/v1/register/ | POST
    path('login/' , SignInAPI.as_view() , name='login'),

    #domain.dn/api/v1/user | GET
    path('user/', MainUser.as_view() , name='user'),



]