from rest_framework import generics

from . import serializers
from .models import CustomUser, Article


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserListSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserRegistrationSerializer


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer


class ArticleCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.ArticleSerializer
