from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.main, name="main"),
    path("review/", views.review, name="review"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("update/<int:pk>/", views.update, name="update"),
]
