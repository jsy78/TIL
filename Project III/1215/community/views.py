from django.shortcuts import render, redirect
from .models import Community, Comment, Photo
from .forms import CommunityForm, CommentForm, ReCommentForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

@login_required
def index(request):
    posts = Community.objects.order_by("-pk")
    context = {"posts": posts,}
    return render(request, "community/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        post_form = CommunityForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for image in request.FILES.getlist("images"):
                photo = Photo()
                photo.post = post
                photo.image = image
                photo.save()
            return redirect("community:index")
    else:
        post_form = CommunityForm()
    context = {
        "post_form": post_form,
    }
    return render(request, "community/create.html", context)


@login_required
def detail(request, community_pk):
    post = get_object_or_404(Community, pk=community_pk)
    comment_form = CommentForm()
    recomment_form = ReCommentForm()
    comment_count = post.comment_set.all().count()

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()
    cookie_value = request.COOKIES.get("hitboard", "_")

    context = {
        "post": post,
        "comment_form": comment_form,
        "comments": post.comment_set.all(),
        "comment_count": comment_count,
        "recomment_form": recomment_form,
    }
    response = render(request, "community/detail.html", context)
    if f"_{community_pk}_" not in cookie_value:
        cookie_value += f"{community_pk}_"
        response.set_cookie("hitboard", value=cookie_value, max_age=max_age, httponly=True)
        post.hits += 1
        post.save()

    return response


@login_required
def update(request, community_pk):
    post = get_object_or_404(Community, pk=community_pk)
    # 커뮤니티의 해당 글의 사진이미지 전체 받아온다.
    photo_list = post.photo_set.all()
    if post.user == request.user:
        if request.method == "POST":
            post_form = CommunityForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.save()

                if request.FILES.getlist("images"):
                    for image in photo_list:
                        image.delete()
                    # 이미지 삭제(초기화)하고 난뒤 이미지 저장
                    for image in request.FILES.getlist("images"):
                        photo = Photo()
                        photo.post = post
                        photo.image = image
                        photo.save()

                    return redirect("community:detail", post.pk)
                else:
                    if request.POST.getlist("image-clear"):
                        for img in photo_list:
                            img.delete()
                    return redirect("community:detail", post.pk)
        else:
            post_form = CommunityForm(instance=post)
        context = {
            'post':post,
            "post_form": post_form,
            "photo_list": photo_list,
        }
        return render(request, "community/update.html", context)
    else:
        return HttpResponseForbidden()


@login_required
def delete(request, community_pk):
    post = get_object_or_404(Community, pk=community_pk)

    if post.user == request.user:
        if request.method == "POST":
            post.delete()
            return redirect("community:index")
    else:
        return HttpResponseForbidden()


@login_required
def comments_create(request, community_pk):
    post = get_object_or_404(Community, pk=community_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.posting = post
            comment.user = request.user
            comment.save()
        return redirect("community:detail", post.pk)


@login_required
def comments_update(request, community_pk, comment_pk):
    post = get_object_or_404(Community, pk=community_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.posting = post
            comment.user = request.user
            comment.save()
        return redirect("community:detail", community_pk)
    else:
        comment_form = CommentForm(instance=comment)
        return redirect("community:detail", community_pk)


@login_required
def comments_delete(request, community_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
        return redirect("community:detail", community_pk)
    else:
        return HttpResponseForbidden()


@login_required
def recomments_create(request, community_pk, comment_pk):
    post = get_object_or_404(Community, pk=community_pk)
    if request.user.is_authenticated:
        recomment_form = ReCommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.posting = post
            recomment.user = request.user
            recomment.parent_comment_id = comment_pk
            recomment.save()

        return redirect("community:detail", post.pk)


@login_required
def recomments_update(request, community_pk, comment_pk, recomment_pk):
    post = get_object_or_404(Community, pk=community_pk)
    recomment = Comment.objects.get(pk=recomment_pk)
    if request.method == "POST":
        recomment_form = ReCommentForm(request.POST, instance=recomment)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.posting = post
            recomment.user = request.user
            recomment.parent_comment_id = comment_pk
            recomment.save()
        return redirect("community:detail", community_pk)
    else:
        recomment_form = ReCommentForm(instance=recomment)
        return redirect("community:detail", community_pk)


@login_required
def recomments_delete(request, community_pk, recomment_pk):
    recomment = get_object_or_404(Comment, pk=recomment_pk)

    if request.user == recomment.user:
        recomment.delete()
        return redirect("community:detail", community_pk)
    else:
        return HttpResponseForbidden()


@login_required
def like(request, community_pk):
    post = get_object_or_404(Community, pk=community_pk)

    if post.like.filter(pk=request.user.pk).exists():
        post.like.remove(request.user)
        is_likes = False
    else:
        post.like.add(request.user)
        is_likes = True
    data = {"is_likes": is_likes, "likes_count": post.like.count()}
    return JsonResponse(data)


@login_required
def comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.like.filter(pk=request.user.pk).exists():
        comment.like.remove(request.user)
        is_likes = False
    else:
        comment.like.add(request.user)
        is_likes = True
    data = {"is_likes": is_likes, "likes_count": comment.like.count()}
    return JsonResponse(data)


