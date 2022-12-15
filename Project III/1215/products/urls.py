from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("product_create/", views.product_create, name="product_create"),
    path("<int:product_pk>/", views.product_detail, name="product_detail"),
    path("<int:product_pk>/product_update/", views.product_update, name="product_update"),
    path("<int:product_pk>/product_delete/", views.product_delete, name="product_delete"),
    path("<int:product_pk>/product_like/", views.product_like, name="product_like"),
    path("<int:product_pk>/comment_create/", views.comment_create, name="comment_create"),
    path("<int:product_pk>/comment_update/<int:comment_pk>/", views.comment_update, name="comment_update"),
    path("<int:product_pk>/comment_delete/<int:comment_pk>/", views.comment_delete, name="comment_delete"),
    path("<int:product_pk>/comment_like/<int:comment_pk>/", views.comment_like, name="comment_like"),
    path("<int:product_pk>/reply_create/<int:comment_pk>/", views.reply_create, name="reply_create"),
]
