from django.contrib import admin

from article.models import Comment, Article


admin.site.register(Article)
admin.site.register(Comment)
