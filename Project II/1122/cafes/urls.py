from django.urls import path
from . import views

app_name = "cafes"

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<article_category>/", views.category, name="category"),
    path("<int:article_pk>/", views.cafe_detail, name="cafe_detail"),
    path("<int:article_pk>/new/", views.cafe_detail_new, name="cafe_detail_new"),
    path("<int:article_pk>/good/", views.cafe_detail_good, name="cafe_detail_good"),
    path("cafe_create/", views.cafe_create, name="cafe_create"),
    path("<int:article_pk>/cafe_update/", views.cafe_update, name="cafe_update"),
    path("<int:article_pk>/cafe_delete/", views.cafe_delete, name="cafe_delete"),
    path("<int:article_pk>/cafe_like/", views.cafe_like, name="cafe_like"),
    path("<int:article_pk>/cafe_bookmark/", views.cafe_bookmark, name="cafe_bookmark"),
    path("cafe_search/", views.cafe_search, name="cafe_search"),
    path("<int:article_pk>/review_create/", views.review_create, name="review_create"),
    path("<int:article_pk>/review_update/<int:review_pk>/", views.review_update, name="review_update"),
    path("<int:article_pk>/review_delete/<int:review_pk>/", views.review_delete, name="review_delete"),
    path("<int:article_pk>/review_like/<int:review_pk>/", views.review_like, name="review_like"),
    path("<int:review_pk>/comment_create/", views.comment_create, name="comment_create"),
    path("<int:review_pk>/comment_update/<int:comment_pk>/", views.comment_update, name="comment_update"),
    path("<int:review_pk>/comment_delete/<int:comment_pk>/", views.comment_delete, name="comment_delete"),
    path("<int:review_pk>/comment_like/<int:comment_pk>/", views.comment_like, name="comment_like"),
    path("<int:review_pk>/reply_create/<int:comment_pk>/", views.reply_create, name="reply_create"),
]
