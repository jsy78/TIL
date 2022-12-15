from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from django.contrib.auth import get_user_model
from hobby.models import Hobby
from products.models import Product
from django.db.models import Avg, Count, Max, Case, When, IntegerField, Q
from django.core.paginator import Paginator


@require_safe
def main(request):
    if request.user.is_authenticated:
        user = request.user
        # 유저 태그 모두 저장
        my_tags = []
        for i in user.sports:
            my_tags.append(i)
        for i in user.travel:
            my_tags.append(i)
        for i in user.art:
            my_tags.append(i)
        for i in user.food:
            my_tags.append(i)
        for i in user.develop:
            my_tags.append(i)
        
        posts_new = Hobby.objects.all().order_by("-pk")[:3].annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
        posts_hit = Hobby.objects.all().order_by("-hits")[:3].annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
        posts_like = Hobby.objects.filter(tags__in=my_tags)[:3].annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
        
        Products = Product.objects.all().order_by("-hits")[:16]

        page = request.GET.get("page", "1")
        paginator = Paginator(Products, 8)
        page_obj = paginator.get_page(page)


        context = {
            'posts_new': posts_new,
            'posts_hit' : posts_hit,
            'posts_like' :posts_like,
            'products' : Products,
            'page_obj' : page_obj,
        }
        return render(request, "main.html", context)
    else:
        return redirect('accounts:login')

