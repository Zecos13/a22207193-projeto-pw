from django.contrib import admin
from .models import Author, Article, Comment, Rating


# Register your models here.

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)