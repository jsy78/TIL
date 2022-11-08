from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm, ReplyForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta, timezone
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import locale

# 로케일 한국어 설정 (요일을 한글로 표시하기 위함)
locale.setlocale(locale.LC_ALL, "")

# Create your views here.


def index(request):
    page = request.GET.get("page", "1")  # 페이지
    articles = Article.objects.order_by("-pk")
    paginator = Paginator(articles, 5)
    page_list = paginator.get_page(page)
    context = {
        "articles": articles,
        "page_list": page_list,
    }
    return render(request, "articles/index.html", context)


@login_required
def saved(request):
    page = request.GET.get("page", "1")  # 페이지
    articles = (
        get_user_model()
        .objects.prefetch_related(
            Prefetch(
                "bookmark_articles", queryset=Article.objects.select_related("user")
            )
        )
        .get(pk=request.user.pk)
        .bookmark_articles.order_by("-pk")
    )
    paginator = Paginator(articles, 10)
    page_list = paginator.get_page(page)
    context = {
        "articles": articles,
        "page_list": page_list,
    }
    return render(request, "articles/saved.html", context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    cookie_value = request.COOKIES.get("hits", "_")

    if f"_{pk}_" not in cookie_value:
        article.hits += 1
        article.save()

    context = {
        "article": article,
        "comments": Comment.objects.select_related("user").filter(
            article=article, parent=None
        ),
        "comments_count": Comment.objects.filter(article=article).count(),
        "comment_form": CommentForm(),
        "reply_form": ReplyForm(),
    }
    response = render(request, "articles/detail.html", context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    if f"_{pk}_" not in cookie_value:
        cookie_value += f"_{pk}_"
        response.set_cookie("hits", value=cookie_value, max_age=max_age, httponly=True)

    return response


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        location = request.POST.get("location")
        roadname = request.POST.get("roadname")
        if request.POST.get("grade") == "" or request.POST.get("grade") == 0:
            grade = 0.5
        else:
            grade = float(request.POST.get("grade"))
        if (
            form.is_valid()
            and 0.5 <= grade <= 5
            and 0 < len(location) <= 120
            and 0 < len(roadname) <= 30
        ):
            article = form.save(commit=False)
            article.user = request.user
            article.location = location
            article.roadname = roadname
            article.grade = grade
            article.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
        "grade": 5,
        "location": "",
        "roadname": "",
    }
    return render(request, "articles/form.html", context)


@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            location = request.POST.get("location")
            roadname = request.POST.get("roadname")
            if request.POST.get("grade") == "" or request.POST.get("grade") == 0:
                grade = 0.5
            else:
                grade = float(request.POST.get("grade"))
            if (
                form.is_valid()
                and 0.5 <= grade <= 5
                and 0 < len(location) <= 120
                and 0 < len(roadname) <= 30
            ):
                article = form.save(commit=False)
                article.is_updated = True
                article.location = location
                article.roadname = roadname
                article.grade = grade
                article.save()
                messages.success(request, "글이 수정되었습니다.")
                return redirect("articles:detail", pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            "form": form,
            "grade": article.grade,
            "location": article.location,
            "roadname": article.roadname,
        }
        return render(request, "articles/form.html", context)
    else:
        messages.warning(request, "글 작성자만 수정이 가능합니다.")
        return redirect("articles:detail", pk)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        messages.success(request, "성공적으로 삭제되었습니다.")
        return redirect("articles:index")
    else:
        messages.warning(request, "권한이 없습니다. 작성자만 삭제 가능합니다.")
        return redirect("articles:detail", article.pk)


@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()

            queryset = Comment.objects.select_related("user").filter(article=article)
            queryset_list = list()
            for query in queryset:
                if query.parent == None:
                    queryset_list.append(
                        {
                            "pk": query.pk,
                            "parent": None,
                            "content": query.content,
                            "created_at": query.created_string
                            or query.created_at.astimezone(
                                timezone(timedelta(hours=9))
                            ).strftime("%Y-%m-%d %A"),
                            "username": query.user.username,
                        }
                    )
                else:
                    queryset_list.append(
                        {
                            "pk": query.pk,
                            "parent": query.parent.pk,
                            "content": query.content,
                            "created_at": query.created_string
                            or query.created_at.astimezone(
                                timezone(timedelta(hours=9))
                            ).strftime("%Y-%m-%d %A"),
                            "username": query.user.username,
                        }
                    )

            context = {
                "comments_count": queryset.count(),
                "comments": queryset_list,
                "article_pk": article.pk,
                "request_is_authenticated": request.user.is_authenticated,
                "request_username": request.user.username,
            }
            print(context["comments"])
            return JsonResponse(context)
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
            return redirect("articles:detail", article.pk)
    else:
        messages.warning(request, "로그인이 필요합니다.")
        return redirect("accounts:login")


@require_POST
def reply_create(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    parent_comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user.is_authenticated:
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.article = article
            reply.parent = parent_comment
            reply.user = request.user
            reply.save()

            queryset = Comment.objects.select_related("user").filter(article=article)
            queryset_list = list()
            for query in queryset:
                if query.parent == None:
                    queryset_list.append(
                        {
                            "pk": query.pk,
                            "parent": None,
                            "content": query.content,
                            "created_at": query.created_string
                            or query.created_at.astimezone(
                                timezone(timedelta(hours=9))
                            ).strftime("%Y-%m-%d %A"),
                            "username": query.user.username,
                        }
                    )
                else:
                    queryset_list.append(
                        {
                            "pk": query.pk,
                            "parent": query.parent.pk,
                            "content": query.content,
                            "created_at": query.created_string
                            or query.created_at.astimezone(
                                timezone(timedelta(hours=9))
                            ).strftime("%Y-%m-%d %A"),
                            "username": query.user.username,
                        }
                    )

            context = {
                "comments_count": queryset.count(),
                "comments": queryset_list,
                "article_pk": article.pk,
                "request_is_authenticated": request.user.is_authenticated,
                "request_username": request.user.username,
            }
            return JsonResponse(context)
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
            return redirect("articles:detail", article.pk)
    else:
        messages.warning(request, "로그인이 필요합니다.")
        return redirect("accounts:login")


@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == "POST":
        if request.user == comment.user:
            comment.delete()
            queryset = Comment.objects.select_related("user").filter(article=article)
            queryset_list = list()
            for query in queryset:
                if query.parent == None:
                    queryset_list.append(
                        {
                            "pk": query.pk,
                            "parent": None,
                            "content": query.content,
                            "created_at": query.created_string
                            or query.created_at.astimezone(
                                timezone(timedelta(hours=9))
                            ).strftime("%Y-%m-%d %A"),
                            "username": query.user.username,
                        }
                    )
                else:
                    queryset_list.append(
                        {
                            "pk": query.pk,
                            "parent": query.parent.pk,
                            "content": query.content,
                            "created_at": query.created_string
                            or query.created_at.astimezone(
                                timezone(timedelta(hours=9))
                            ).strftime("%Y-%m-%d %A"),
                            "username": query.user.username,
                        }
                    )

        context = {
            "comments_count": queryset.count(),
            "comments": queryset_list,
            "article_pk": article.pk,
            "request_is_authenticated": request.user.is_authenticated,
            "request_username": request.user.username,
        }
        return JsonResponse(context)
    else:
        messages.warning(request, "댓글 작성자만 삭제 가능합니다.")
        return redirect("articles:detail", article_pk)


@login_required
def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    context = {
        "is_liked": is_liked,
        "like_count": article.like_users.count(),
    }
    return JsonResponse(context)
    # return redirect("articles:detail", article_pk)


@login_required
def bookmark(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user in article.bookmark_users.all():
        article.bookmark_users.remove(request.user)
        is_saved = False
    else:
        article.bookmark_users.add(request.user)
        is_saved = True
    context = {
        "is_saved": is_saved,
        "save_count": article.bookmark_users.count(),
    }
    return JsonResponse(context)
    # return redirect("articles:detail", article_pk)
