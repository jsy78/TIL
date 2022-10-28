from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .form import ReviewForm, CommentForm
from django.contrib import messages

# Create your views here.

def index(request):
    articles = Review.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect('articles:index')
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = get_object_or_404(Review, pk=pk)
    comments = Comment.objects.filter(article=article)
    form = CommentForm()
    context = {
        'article':article,
        'comment_form': form,
        'comments':comments
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = get_object_or_404(Review, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = ReviewForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'articles/form.html', context)
    else:
        messages.warning(request, '본인의 글만 수정할 수 있습니다.')
        return redirect('articles:detail', pk)

@login_required
def delete(request, pk):
    article = get_object_or_404(Review, pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    else:
        messages.warning(request, '본인의 글만 삭제할 수 있습니다.')
        return redirect('articles:detail', pk)

@login_required
def like(request, pk):
    article = get_object_or_404(Review, pk=pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': article.like_users.count() }
    return JsonResponse(context)

@login_required
def comment_create(request, pk):
    article = get_object_or_404(Review, pk=pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
        return JsonResponse(context)

@login_required
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('articles:detail', pk)
    else:
        messages.warning(request, '본인의 댓글만 삭제할 수 있습니다.')
        return redirect('articles:detail', pk)

def search(request):
    search = request.GET.get("search")
    select = request.GET.get('select')
    if select == '2':
        articles = Review.objects.filter(title__icontains=search)
    else:
        articles = Review.objects.filter(user__username__icontains=search)
    context = {
        "articles" : articles,
    }
    return render(request, 'articles/search.html', context) 