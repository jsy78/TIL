from django.urls import path
from . import views

app_name = "hobby"

urlpatterns = [
    path("create", views.create, name="create"),
    path('save/', views.save, name='save'),
    path('<int:hobby_pk>', views.detail, name='detail'),
    path('<int:hobby_pk>/call', views.call, name='call'),
    path('<int:hobby_pk>/<int:user_pk>/approve', views.approve, name='approve'),
    path('<int:hobby_pk>/<int:user_pk>/reject', views.reject, name='reject'),
    path('<int:hobby_pk>/comment_create', views.comment_create, name='comment_create'),
    path("index/<str:category_name>/", views.index, name="index"),
    path("index/tag/<str:tag_name>/", views.tag, name="tag"),
    path('<int:hobby_pk>/like_hobby', views.like_hobby, name='like_hobby'),
    path('<int:comment_pk>/like_comment', views.like_comment, name='like_comment'),
    path('<int:comment_pk>/comment_delete',views.comment_delete, name='comment_delete'),
    path('<int:hobby_pk>/delete_hobby', views.delete_hobby, name='delete_hobby'),
    path('<int:hobby_pk>/update', views.update, name='update'),
]
