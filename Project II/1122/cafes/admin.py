from django.contrib import admin
from .models import Article, Review, Comment

# Register your models here.
# https://docs.djangoproject.com/en/3.2/intro/tutorial07/
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "address",
        "created_time",
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "cafe",
        "title",
        "content",
        "created_time",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "review",
        "content",
        "created_time",
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)