from django.urls import include, path

from .views import ArticleListAPIView, \
                   CommentCreateAPIView, \
                   CommentNestedAPIView, \
                   CommentToArticleAPIView, \
                   UserCreateAPIView, \
                   UserListAPIView

urlpatterns = [
    path('articles', ArticleListAPIView.as_view(), name='get_articles_list'),
    path('articles/<int:id>/comments', CommentToArticleAPIView.as_view(), name='get_comments_by_article'),
    path('comments/nested/<int:id>', CommentNestedAPIView.as_view(), name='get_nested_comments_by_parent_comment'),
    path('comments', CommentCreateAPIView.as_view(), name='create_comment'),
    path('users', UserListAPIView.as_view(), name='get_users_list'),
    path('users', UserCreateAPIView.as_view(), name='create_user'),
    path('auth', include('djoser.urls.authtoken')),
    path('auth', include('djoser.urls.jwt')),
]
