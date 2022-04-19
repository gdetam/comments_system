from django.contrib.auth.models import AbstractUser
from django.db import models

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """class CustomUser create structure object user."""

    username = models.CharField(max_length=100, unique=True,
                                verbose_name='Никнейм')
    email = models.EmailField(max_length=100, unique=True,
                              verbose_name='Электронная почта')

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'
        ordering = ['id']


class Article(models.Model):
    """class Article create structure object article."""

    title = models.CharField(max_length=100, unique=True,
                             verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Время создания')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='authors')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'
        ordering = ['id']


class Comment(MPTTModel):
    """class Comment create structure object comment."""

    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comment'
        ordering = ['id']
