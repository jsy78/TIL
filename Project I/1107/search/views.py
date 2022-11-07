from django.shortcuts import render
from articles.models import Article
from accounts.models import User
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def searchResult(request):
    # user = None
    article = None
    query = None
    if "q" in request.GET:
        query = request.GET.get("q")
        # user = User.objects.all().filter(Q(username__contains=query))
        article = Article.objects.order_by("-pk").filter(
            Q(title__contains=query)
            | Q(content__contains=query)
            | Q(location__contains=query)
            | Q(foodType__contains=query)
        )
    context = {
        "query": query,
        # "user": user,
        "article": article,
    }
    return render(
        request,
        "search/search.html",
        context,
    )
