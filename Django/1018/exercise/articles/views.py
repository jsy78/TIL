from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "게시글 추가 완료")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context=context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
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
    }
    return render(request, "articles/form.html", context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        article.delete()
        messages.warning(request, "게시글 삭제 완료")
        return redirect("articles:index")
    else:
        return redirect("articles:detail", article.pk)


def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        messages.success(request, "댓글 추가 완료")
    return redirect("articles:detail", article.pk)


def comment_update(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    updated_comment = request.POST.get("updated_comment")
    if 0 < len(updated_comment) <= 80:
        comment.content = updated_comment
        comment.article = article
        comment.save()
        messages.success(request, "댓글 수정 완료")
    return redirect("articles:detail", article.pk)


def comment_delete(request, article_pk, comment_pk):
    if request.method == "POST":
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        messages.warning(request, "댓글 삭제 완료")
    return redirect("articles:detail", article_pk)
