from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Comment, CustomUser
from .serializers import ArticleListSerializer, \
                         CommentCreateSerializer, \
                         CommentNestedSerializer, \
                         CommentToArticleSerializer, \
                         UserListSerializer, \
                         UserRegistrationSerializer


class UserListAPIView(generics.ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer


class UserCreateAPIView(generics.CreateAPIView):

    serializer_class = UserRegistrationSerializer


class ArticleListAPIView(generics.ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class CommentToArticleAPIView(APIView):

    def get(self, request, pk):
        comment = Comment.objects.filter(article_id=pk, level=0)
        serializer = CommentToArticleSerializer(comment, many=True)
        return Response(serializer.data)


class CommentNestedAPIView(APIView):

    def get(self, request, pk):
        comment = Comment.objects.get(id=pk).get_children()
        serializer = CommentNestedSerializer(comment, many=True)
        return Response(serializer.data)


class CommentCreateAPIView(generics.CreateAPIView):

    serializer_class = CommentCreateSerializer
