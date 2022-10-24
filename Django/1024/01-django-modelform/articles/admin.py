from django.contrib import admin
from .models import Article, Comment

# Register your models here.
# https://docs.djangoproject.com/en/3.2/intro/tutorial07/
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at', 'updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display  = ('content', 'created_at', 'article')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)