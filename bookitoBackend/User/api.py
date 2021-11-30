from django.contrib import auth
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission , User  , Group
from books.models import Category , Author

class SignUpAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_perm = User.objects.get(id=user.id)

        # restrict user from changing , deleting , adding Category & Author
        content_type_category = ContentType.objects.get_for_model(Category)
        permission_read_category = Permission.objects.get(codename='view_category',content_type=content_type_category)
        user_perm.user_permissions.add(permission_read_category)
        content_type_author = ContentType.objects.get_for_model(Author)
        permission_read_author = Permission.objects.get(codename='view_author',content_type=content_type_author)
        user_perm.user_permissions.add(permission_read_category)

        token = AuthToken.objects.create(user)
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        },status.HTTP_201_CREATED)


class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class MainUser(generics.RetrieveAPIView):
  permission_classes = [
      permissions.IsAuthenticated
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user