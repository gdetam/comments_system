from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.ArticleListAPIView.as_view(), name='articles_list'),
    path('articles/<int:pk>/', views.ArticleDetailAPIView.as_view(), name='articles_detail'),
    path('articles/create/', views.ArticleCreateAPIView.as_view(), name='articles_create'),
    path('users/', views.UserListAPIView.as_view(), name='user_list'),
    path('users/create/', views.UserCreateAPIView.as_view(), name='user_create'),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
