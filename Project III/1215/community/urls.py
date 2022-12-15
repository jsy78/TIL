from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<int:community_pk>/detail", views.detail, name="detail"),
    path("<int:community_pk>/update", views.update, name="update"),
    path("<int:community_pk>/delete", views.delete, name="delete"),
    path("<int:community_pk>/comments", views.comments_create, name="comments_create"),
    path("<int:community_pk>/comments/<int:comment_pk>/update/", views.comments_update, name="comments_update"),
    path("<int:community_pk>/comments/<int:comment_pk>/delete/", views.comments_delete, name="comments_delete"),
    path("<int:community_pk>/recomments/<int:comment_pk>", views.recomments_create, name="recomments_create"),
    path("<int:community_pk>/recomments/<int:comment_pk>/<int:recomment_pk>/update", views.recomments_update, name="recomments_update"),
    path("<int:community_pk>/recomments/<int:recomment_pk>/delete", views.recomments_delete, name="recomments_delete"),
    path("<int:community_pk>/like/", views.like, name="like"),
    path("<int:comment_pk>/comment_like/", views.comment_like, name="comment_like"),
]
