from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/<int:todo_pk>/", views.update, name="update"),
    path("modify/<int:todo_pk>/", views.modify, name="modify"),
    path("delete/<int:todo_pk>/", views.delete, name="delete"),
]
