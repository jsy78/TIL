from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.index, name="index"),
    path("received_box/", views.received_box, name="received_box"),
    path("sent_box/", views.sent_box, name="sent_box"),
    path("important_box/", views.important_box, name="important_box"),
    path("trash_box/", views.trash_box, name="trash_box"),
    path("send/", views.send, name="send"),
    path("received_note/<int:received_note_pk>/", views.received_note_detail, name="received_note_detail"),
    path("sent_note/<int:sent_note_pk>/", views.sent_note_detail, name="sent_note_detail"),
    path("received_note/<int:received_note_pk>/important/", views.important, name="important"),
    path("received_note/<int:received_note_pk>/trash/", views.trash, name="trash"),
    path("received_note/<int:received_note_pk>/delete/", views.received_note_delete, name="received_note_delete"),
    path("sent_note/<int:sent_note_pk>/delete/", views.sent_note_delete, name="sent_note_delete"),
]
