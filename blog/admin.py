from django.contrib import admin
from .models import Article, Comment, CustomUser


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(CustomUser)
