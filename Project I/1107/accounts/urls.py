from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
    path("mypage/", views.mypage, name="mypage"),
    path("followings/", views.followings, name="followings"),
    path("follow/<username>/", views.follow, name="follow"),
    path("profile/<username>/", views.profile, name="profile"),
]
