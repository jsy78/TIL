from django.urls import path
from . import views

app_name = "letters"

urlpatterns = [
    path("", views.index, name="index"),
    path("email_send/", views.email_send, name="email_send"),
    path("<int:pk>/", views.email_detail, name="email_detail"),
    path("<int:pk>/trash_throw_away/", views.trash_throw_away, name="trash_throw_away"),
    path("<int:pk>/trash_return/", views.trash_return, name="trash_return"),
    path("trash_can/", views.trash_can, name="trash_can"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("important/", views.important, name="important"),
    path("send_can/", views.send_can, name="send_can"),
    path("<int:pk>/important_check/", views.important_check, name="important_check"),
    path("<int:pk>/important_return/", views.important_return, name="important_return"),
    path("<int:pk>/click_email_send", views.click_email_send, name="click_email_send"),
]
