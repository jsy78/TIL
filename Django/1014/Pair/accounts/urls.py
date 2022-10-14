from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.index, name="index"),
    path("mypage/", views.mypage, name="mypage"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("password/", views.password, name="password"),
    path("delete/", views.delete, name="delete"),
    path("articles/", views.articles, name="articles"),
]
