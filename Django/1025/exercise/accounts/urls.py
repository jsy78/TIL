from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("follow/<int:pk>/", views.follow, name="follow"),
    path("following/<int:pk>/", views.following, name="following"),
    path("follower/<int:pk>/", views.follower, name="follower"),
    path("profile/<username>/", views.profile, name="profile"),
    path("profile/<username>/article", views.article, name="article"),
    path("profile/<username>/comment", views.comment, name="comment"),
    path("profile/<username>/article/like/", views.like_article, name="like_article"),
    path("profile/<username>/comment/like/", views.like_comment, name="like_comment"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
]
