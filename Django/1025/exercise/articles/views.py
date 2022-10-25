from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

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
    else:
        article.like_users.add(request.user)
    return redirect("articles:detail", article.pk)


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
            messages.success(request, "댓글 추가 완료")
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
        return redirect("articles:detail", article.pk)
    
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
            comment.article = article
            comment.save()
            messages.success(request, "댓글 수정 완료")
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
        return redirect("articles:detail", article.pk)

    messages.warning(request, "로그인이 필요합니다.")
    return redirect('accounts:login')
    


@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user.is_authenticated:
        if request.user != comment.user:
            messages.warning(request, "권한이 없습니다.")
            return redirect("articles:detail", article_pk)

        comment.delete()
        messages.warning(request, "댓글 삭제 완료")
        return redirect("articles:detail", article_pk)

    messages.warning(request, "로그인이 필요합니다.")
    return redirect('accounts:login')


@login_required
def comment_like(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.like_users.filter(pk=request.user.pk).exists():  
  # if request.user in comment.like_users.all():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect("articles:detail", article.pk)