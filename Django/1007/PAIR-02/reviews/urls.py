from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    # http://127.0.0.1:8000/reviews/
    path("", views.index, name="index"),
    # http://127.0.0.1:8000/reviews/create/
    path("create/", views.create, name="create"),
    # http://127.0.0.1:8000/reviews/<int:pk>/
    path("<int:pk>/", views.detail, name="detail"),
    # http://127.0.0.1:8000/reviews/<int:pk>/update/
    path("<int:pk>/update/", views.update, name="update"),
    # http://127.0.0.1:8000/reviews/<int:pk>/delete/
    path("<int:pk>/delete/", views.delete, name="delete"),
]
