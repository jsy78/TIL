from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("saved/", views.saved, name="saved"),
    path("<int:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path(
        "<int:article_pk>/comments/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path("<int:article_pk>/likes/", views.likes, name="likes"),
    path("<int:article_pk>/bookmark/", views.bookmark, name="bookmark"),
    path(
        "<int:article_pk>/comments/<int:comment_pk>/reply/",
        views.reply_create,
        name="reply_create",
    ),
]
