from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Article, Comment, CustomUser


class FilterCommentSerializer(serializers.ListSerializer):
    """Comments filter only parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Recursive children comments list"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class UserListSerializer(serializers.ModelSerializer):
    """Serializer for user list"""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class UserRegistrationSerializer(UserCreateSerializer):
    """Serializer for registration user"""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email') + ('password',)


class ArticleListSerializer(serializers.ModelSerializer):
    """Serializer for article list"""

    class Meta:
        model = Article
        fields = ('id', 'title', 'description')


class CommentCreateSerializer(serializers.ModelSerializer):
    """Serializer for create comment to article"""

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for create comment to comment and recursive representation"""

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comment
        fields = ('name', 'text', 'children')


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail article"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'author', 'comments')
