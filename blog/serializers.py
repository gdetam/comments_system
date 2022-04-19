from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Article, Comment, CustomUser


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email') + ('password',)


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'description')


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class ArticleDetailSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentCreateSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'author', 'comments')
