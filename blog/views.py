from rest_framework import generics

from . import serializers
from .models import CustomUser, Article
from .serializers import CommentCreateSerializer


class UserListAPIView(generics.ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserListSerializer


class UserCreateAPIView(generics.CreateAPIView):

    serializer_class = serializers.UserRegistrationSerializer


class ArticleListAPIView(generics.ListAPIView):

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer


class ArticleDetailAPIView(generics.RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleDetailSerializer


class CommentCreateAPIView(generics.CreateAPIView):

    serializer_class = CommentCreateSerializer
