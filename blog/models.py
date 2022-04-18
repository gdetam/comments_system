from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    username = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Никнейм'
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='Электронная почта'
    )

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Blablog user'
        verbose_name_plural = 'Blablog user'
        ordering = ['id']


class Article(models.Model):

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='Автор'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Blablog article'
        verbose_name_plural = 'Blablog article'
        ordering = ['id']
