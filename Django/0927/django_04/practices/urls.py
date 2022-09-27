from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index),
    path("ping/", views.ping),
    path("pong/", views.pong),
]
