from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Article, CustomUser


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


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'
