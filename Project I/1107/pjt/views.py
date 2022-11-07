from django.shortcuts import render
from articles.models import Article
from django.db.models import Count


def main(request):
    articles = Article.objects.annotate(like_count=Count("like_users")).order_by(
        "-like_count"
    )
    context = {
        "articles": articles,
    }
    return render(request, "main.html", context)


def new(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "main.html", context)


def good(request):
    articles = Article.objects.annotate(like_count=Count("like_users")).order_by(
        "-like_count"
    )
    context = {
        "articles": articles,
    }
    return render(request, "main.html", context)


def hit(request):
    articles = Article.objects.order_by("-hits")
    context = {
        "articles": articles,
    }
    return render(request, "main.html", context)
