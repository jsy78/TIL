from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.http import JsonResponse
from django.core import serializers
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from datetime import timedelta, timezone
import locale
import json

locale.setlocale(locale.LC_ALL, '')

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "게시글 추가 완료")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.user != article.user:
        messages.warning(request, "권한이 없습니다.")
        return redirect("articles:detail", article.pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "게시글 수정 완료")
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article_pk": article.pk,
    }
    return render(request, "articles/update.html", context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.user.is_authenticated:
        if request.user != article.user:
            messages.warning(request, "권한이 없습니다.")
            return redirect("articles:detail", article.pk)

        article.delete()
        messages.success(request, "게시글 삭제 완료")
        return redirect("articles:index")
    messages.warning(request, "로그인이 필요합니다.")
    return redirect('accounts:login')
           

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if article.like_users.filter(pk=request.user.pk).exists(): 
  # if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_article_liked = False
    else:
        article.like_users.add(request.user)
        is_article_liked = True
    context = {
        "is_article_liked": is_article_liked, 
        "article_like_count": article.like_users.count(),
    }
    return JsonResponse(context)


@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()

            comments_json = json.loads(serializers.serialize('json', article.comment_set.all(), ensure_ascii=False))
            for dic in comments_json :
                dic["fields"]["created_at"] = Comment.objects.get(pk=dic['pk']).created_at.astimezone(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %p %I:%M')
                dic["fields"]["updated_at"] = Comment.objects.get(pk=dic['pk']).updated_at.astimezone(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %p %I:%M')
                dic["fields"]["username"] = get_user_model().objects.get(pk=dic["fields"]["user"]).username

            context = {
                "comments_count": article.comment_set.count(),
                "comments_json": comments_json,
                "request_user": request.user.pk,
            }
            return JsonResponse(context)
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
            return redirect("articles:detail", article.pk)
    else:
        messages.warning(request, "로그인이 필요합니다.")
        return redirect('accounts:login')


@require_POST
def comment_update(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user.is_authenticated:
        if request.user != comment.user:
            messages.warning(request, "권한이 없습니다.")
            return redirect("articles:detail", article.pk)

        updated_comment = request.POST.get("updated_comment")
        if 0 < len(updated_comment) <= 80:
            comment.content = updated_comment
            comment.save()
            context = {
                'content': comment.content,
                'updated': comment.updated_at.astimezone(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %p %I:%M'),
            }
            return JsonResponse(context)
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
            return redirect("articles:detail", article.pk)
    else:
        messages.warning(request, "로그인이 필요합니다.")
        return redirect('accounts:login')
    


@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user.is_authenticated:
        if request.user != comment.user:
            messages.warning(request, "권한이 없습니다.")
            return redirect("articles:detail", article_pk)

        comment.delete()
        comments_json = json.loads(serializers.serialize('json', article.comment_set.all(), ensure_ascii=False))
        for dic in comments_json :
            dic["fields"]["created_at"] = Comment.objects.get(pk=dic['pk']).created_at.astimezone(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %p %I:%M')
            dic["fields"]["updated_at"] = Comment.objects.get(pk=dic['pk']).updated_at.astimezone(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %p %I:%M')
            dic["fields"]["username"] = get_user_model().objects.get(pk=dic["fields"]["user"]).username

        context = {
            "comments_count": article.comment_set.count(),
            "comments_json": comments_json,
            "request_user": request.user.pk,
        }
        return JsonResponse(context)

    messages.warning(request, "로그인이 필요합니다.")
    return redirect('accounts:login')


@login_required
def comment_like(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.like_users.filter(pk=request.user.pk).exists():  
  # if request.user in comment.like_users.all():
        comment.like_users.remove(request.user)
        is_comment_liked = False
    else:
        comment.like_users.add(request.user)
        is_comment_liked = True
    context = {
        "is_comment_liked": is_comment_liked, 
        "comment_like_count": comment.like_users.count(),
    }
    return JsonResponse(context)