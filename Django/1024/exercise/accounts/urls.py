from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("profile/article", views.article, name="article"),
    path("profile/comment", views.comment, name="comment"),
    path("profile/like/article", views.like_article, name="like_article"),
    path("profile/like/comment", views.like_comment, name="like_comment"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
]
