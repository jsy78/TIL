from django.shortcuts import render
from cafes.models import Article, Review
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator
from django.db.models import Count, Avg


@require_safe
def main(request):
    articles = (
        Article.objects.order_by("-pk")
        .annotate(reviews_count=Count("review"))
        .annotate(average_rate=Avg("review__rate"))
    )
    page = request.GET.get("page", "1")
    paginator = Paginator(articles, 6)
    page_obj = paginator.get_page(page)

    print("page_ob ", page_obj)
    print("paginator ", paginator)
    print("article ", articles)

    context = {
        "articles": articles,
        "page_obj": page_obj,
    }
    return render(request, "main.html", context)
