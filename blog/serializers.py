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


class RecursiveCommentsSerializer(serializers.Serializer):
    """Recursive children comments list"""

    def to_representation(self, value):
        if value.level <= 2:
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


class CommentNestedSerializer(serializers.ModelSerializer):
    """List of nested comments by parent comment"""

    children = RecursiveSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('level', 'name', 'text', 'children')


class CommentToArticleSerializer(serializers.ModelSerializer):
    """Get comments by article"""

    children = RecursiveCommentsSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('id', 'level', 'name', 'text', 'children')
