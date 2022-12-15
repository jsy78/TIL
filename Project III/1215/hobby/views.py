from django.shortcuts import render, redirect, get_object_or_404
from .forms import HobbyForm, HobbyUpdateForm, AcceptedForm, CommentForm
from .models import Hobby, Accepted, Tag, HobbyComment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, datetime, timedelta
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Avg, Count, Max, Case, When, IntegerField, Q
from django.core.paginator import Paginator
import requests
import json
import os

# Create your views here.

@login_required
def create(request):
    if request.method == "POST":
        form = HobbyForm(request.POST, request.FILES)
        accepted = AcceptedForm()
        if form.is_valid():
            temp = form.save(commit=False)
            temp.host = request.user
            temp.save()
            atemp = accepted.save(commit=False)
            atemp.joined = True
            atemp.hobby = temp
            atemp.user = request.user
            atemp.save()
            return redirect("hobby:detail", temp.pk)
    else:
        form = HobbyForm()
    context = {
        "form": form,
    }
    return render(request, "hobby/form.html", context)

@login_required
def update(request, hobby_pk):
    hobby = get_object_or_404(Hobby, pk=hobby_pk)
    if request.user == hobby.host:
        if request.method == "POST":
            form = HobbyUpdateForm(request.POST, request.FILES, instance=hobby)
            if form.is_valid():
                temp = form.save(commit=False)
                temp.host = request.user
                temp.save()
                return redirect("hobby:detail", temp.pk)
        else:
            form = HobbyUpdateForm(instance=hobby)
        context = {
            "form": form,
        }
        return render(request, "hobby/update.html", context)

@login_required
def detail(request, hobby_pk):
    hobby = Hobby.objects.get(pk=hobby_pk)
    comments = HobbyComment.objects.filter(hobby=hobby, parent=None).order_by('-pk')
    accepted = Accepted.objects.filter(hobby=hobby, joined=True)
    waiting = Accepted.objects.filter(hobby=hobby, joined=False)
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()
    cookie_value = request.COOKIES.get("hitboard", "_")
    context = {
        'hobby':hobby,
        'accepted': accepted,
        'waiting': waiting,
        'comments':comments,
        'comments_len': len(HobbyComment.objects.filter(hobby_id=hobby_pk)),
    }
    response = render(request, "hobby/detail.html", context)
    if f"_{hobby_pk}_" not in cookie_value:
        cookie_value += f"{hobby_pk}_"
        response.set_cookie("hitboard", value=cookie_value, max_age=max_age, httponly=True)
        hobby.hits += 1
        hobby.save()

    return response


# 카테고리별 인기글 , 최신글, 전체 글
@login_required
def index(request, category_name):
    category_posts = (
        Hobby.objects.filter(category=category_name).order_by("-pk").annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
    )
    category_posts_hit = category_posts.order_by("-hits")[:3]

    tags = Tag.objects.filter(category=category_name)

    page = request.GET.get("page", "1")
    paginator = Paginator(category_posts, 4)
    page_obj = paginator.get_page(page)

    context = {
        "category_name": category_name,
        "category_posts": category_posts,
        "category_posts_hit": category_posts_hit,
        'page_obj': page_obj,
        "tags": tags,
    }
    return render(request, "hobby/index.html", context)


# 전체 인기글, 최신글, 태그글 모음
@login_required
def tag(request, tag_name):
    # 로그인한 유저
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
    print(my_tags)
    # 내가 저장한 태그별 허비 보여주기
    tags = []
    category_name = ''
    if tag_name == "likes":
        tag_posts = Hobby.objects.filter(tags__in=my_tags).annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
        print(tag_posts)
    # 조회수 별 허비 보여주기
    elif tag_name == "hits":
        tag_posts = Hobby.objects.all().order_by("-hits").annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
    # 새로 생긴 허비 보여주기
    elif tag_name == "news":
        tag_posts = Hobby.objects.all().order_by("-pk").annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
        print(tag_posts)
    else:
        tag_posts = Hobby.objects.filter(tags=tag_name).annotate(joinmembers=Count("accepted", filter=Q(accepted__joined=True)))
        category_name = Tag.objects.filter(tag=tag_name)[0].category
        tags = Tag.objects.filter(category=category_name)
    page = request.GET.get("page", "1")
    paginator = Paginator(tag_posts, 4)
    page_obj = paginator.get_page(page)
    context = {
        "tags": tags,
        "category_name": category_name,
        "tag_posts": tag_posts,
        "tag_name": tag_name,
        "user": user,
        'page_obj' : page_obj
    }

    return render(request, "hobby/tag.html", context)

@login_required
def call(request, hobby_pk):
    hobby = get_object_or_404(Hobby, pk=hobby_pk)
    accepted = Accepted.objects.filter(hobby=hobby, user=request.user)
    if not accepted.exists():
        aform = AcceptedForm()
        temp = aform.save(commit=False)
        temp.hobby = hobby
        temp.user = request.user
        temp.save()
        res = True
    else:
        res = False
    context = {
        'res': res
    }
    return JsonResponse(context)

@login_required
def approve(request, hobby_pk, user_pk):
    hobby = get_object_or_404(Hobby, pk=hobby_pk)
    accepted = get_object_or_404(Accepted, hobby=hobby, user_id=user_pk)
    accepted_len = Accepted.objects.filter(hobby=hobby, joined=True)
    if request.user == hobby.host:
        if int(hobby.limit) > len(accepted_len):
            accepted.joined = True
            accepted.save()
        else:
            return redirect('hobby:detail', hobby_pk)
    return JsonResponse({'res': True})

@login_required
def reject(request, hobby_pk, user_pk):
    hobby = get_object_or_404(Hobby, pk=hobby_pk)
    if (request.user == hobby.host and user_pk != hobby.host.pk) or request.user.pk == user_pk:
        accepted = get_object_or_404(Accepted, hobby=hobby, user_id=user_pk)
        accepted.delete()
    else:
        print('권한이 없습니다.')
    return redirect('hobby:detail', hobby_pk)

@login_required
def comment_create(request, hobby_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            temp = comment_form.save(commit=False)
            if request.POST['parent']:
                temp.parent_id = int(request.POST['parent'])
            temp.user = request.user
            temp.hobby_id = hobby_pk
            temp.save()
    comments = HobbyComment.objects.filter(hobby_id=hobby_pk, parent=None).order_by('-pk')
    lenComments = len(HobbyComment.objects.filter(hobby_id=hobby_pk))
    comments_data = []
    for comment in comments:
        recomments = comment.recomment.all()
        recomments_data = []
        if len(recomments):
            for recomment in recomments:
                if request.user in recomment.like_user.all():
                    is_like = True
                else: is_like = False
                created_at = recomment.created_at.strftime('%Y-%m-%d %H:%M')
                if recomment.user.image:
                    image = recomment.user.image.url
                else: image = 'https://dummyimage.com/80x80/000/fff'
                recomments_data.append({
                    "pk": recomment.pk,
                    "user": recomment.user.nickname,
                    "user_pk": recomment.user.pk,
                    "content": recomment.content,
                    "created_at": created_at,
                    "is_like": is_like,
                    "image": image,
                    'likeCount': recomment.like_user.count(),
                })

        if request.user in comment.like_user.all():
            is_like = True
        else: is_like = False
        created_at = comment.created_at.strftime('%Y-%m-%d %H:%M')
        if comment.user.image:
            image = comment.user.image.url
        else: image = 'https://dummyimage.com/80x80/000/fff'
        comments_data.append({
            "pk": comment.pk,
            "user": comment.user.nickname,
            "user_pk": comment.user.pk,
            "content": comment.content,
            "created_at": created_at,
            "is_like": is_like,
            "image": image,
            'likeCount': comment.like_user.count(),
            'recomments': recomments_data,
        })
    context = {
        "comments_data": comments_data,
        "comments_len": lenComments
    }
    return JsonResponse(context)

@login_required
def comment_delete(request, comment_pk):
    comment = get_object_or_404(HobbyComment, pk=comment_pk)
    hobby_pk = comment.hobby.pk
    if comment.user == request.user:
        comment.delete()
    else:
        print('권한이 없습니다.')
    comments = HobbyComment.objects.filter(hobby_id=hobby_pk, parent=None).order_by('-pk')
    lenComments = len(HobbyComment.objects.filter(hobby_id=hobby_pk))
    comments_data = []
    for comment in comments:
        recomments = comment.recomment.all()
        recomments_data = []
        if len(recomments):
            for recomment in recomments:
                if request.user in recomment.like_user.all():
                    is_like = True
                else: is_like = False
                created_at = recomment.created_at.strftime('%Y-%m-%d %H:%M')
                if recomment.user.image:
                    image = recomment.user.image.url
                else: image = 'https://dummyimage.com/80x80/000/fff'
                recomments_data.append({
                    "pk": recomment.pk,
                    "user": recomment.user.nickname,
                    "user_pk": recomment.user.pk,
                    "content": recomment.content,
                    "created_at": created_at,
                    "is_like": is_like,
                    "image": image,
                    'likeCount': recomment.like_user.count(),
                })

        if request.user in comment.like_user.all():
            is_like = True
        else: is_like = False
        created_at = comment.created_at.strftime('%Y-%m-%d %H:%M')
        if comment.user.image:
            image = comment.user.image.url
        else: image = 'https://dummyimage.com/80x80/000/fff'
        comments_data.append({
            "pk": comment.pk,
            "user": comment.user.nickname,
            "user_pk": comment.user.pk,
            "content": comment.content,
            "created_at": created_at,
            "is_like": is_like,
            "image": image,
            'likeCount': comment.like_user.count(),
            'recomments': recomments_data,
        })
    context = {
        "comments_data": comments_data,
        "comments_len": lenComments
    }
    return JsonResponse(context)

@login_required
def comment_like(request, comment_pk):
    comment = get_object_or_404(HobbyComment, pk=comment_pk)
    if request.user not in comment.like_user.all():
        comment.like_user.add(request.user)
        is_like = True
    else:
        comment.like_user.remove(request.user)
        is_like = False
    
    data = {
        'is_like': is_like,
        'likeCount': len(comment.like_user.all())   
    }
    return JsonResponse(data)


# 카테고리별 태그 저장
def save(request):
    lsit_1 = [
        "축구",
        "농구",
        "야구",
        "클라이밍",
        "등산",
        "테니스",
        "트래킹",
        "볼링",
        "러닝",
        "스키",
        "보드",
        "헬스",
        "산책",
        "플로깅",
        "자전거",
        "서핑",
        "배드민턴",
        "탁구",
        "골프",
        "스포츠경기",
    ]
    list_2 = [
        "복합문화공간",
        "테마파크",
        "피크닉",
        "드라이브",
        "캠핑",
        "국내여행",
        "해외여행",
    ]
    list_3 = [
        "전시",
        "영화",
        "뮤지컬",
        "공연",
        "디자인",
        "박물관",
        "연극",
        "콘서트",
        "연주회",
        "페스티벌",
    ]

    list_4 = [
        "맛집투어",
        "카페",
        "와인",
        "커피",
        "디저트",
        "맥주",
        "티룸",
        "비건",
        "파인다이닝",
        "요리",
        "페어링",
        "칵테일",
        "위스키",
        "전통주",
    ]
    list_5 = [
        "습관만들기",
        "챌린지",
        "독서",
        "스터디",
        "외국어",
        "재테크",
        "브랜딩",
        "커리어",
        "사이드프로젝트",
    ]
    for i in range(len(lsit_1)):
        tag = Tag()
        tag.tag = lsit_1[i]
        tag.category = "sports"
        tag.save()

    for i in range(len(list_2)):
        tag = Tag()
        tag.tag = list_2[i]
        tag.category = "travel"
        tag.save()
    for i in range(len(list_3)):
        tag = Tag()
        tag.tag = list_3[i]
        tag.category = "art"
        tag.save()
    for i in range(len(list_4)):
        tag = Tag()
        tag.tag = list_4[i]
        tag.category = "food"
        tag.save()
    for i in range(len(list_5)):
        tag = Tag()
        tag.tag = list_5[i]
        tag.category = "develop"
        tag.save()

    return redirect("main")

@login_required    
def like_hobby(request, hobby_pk):
    hobby = get_object_or_404(Hobby, pk=hobby_pk)
    if request.user not in hobby.like_user.all():
        hobby.like_user.add(request.user)
        is_like = True
    else:
        hobby.like_user.remove(request.user)
        is_like = False
    if request.user.image:
        image = request.user.image.url
    else:
        image = 'https://dummyimage.com/80x80/000/fff'
    nickname = request.user.nickname
    user_pk = request.user.pk

    data = {
        'is_like': is_like,
        'likeCount': hobby.like_user.count(),
        'image': image,
        'nickname': nickname,
        'user_pk': user_pk,
    }
    return JsonResponse(data)

@login_required
def like_comment(request, comment_pk):
    comment = get_object_or_404(HobbyComment, pk=comment_pk)
    if request.user not in comment.like_user.all():
        comment.like_user.add(request.user)
        is_like = True
    else:
        comment.like_user.remove(request.user)
        is_like = False
    data = {
        'is_like': is_like,
        'likeCount': comment.like_user.count()
    }
    return JsonResponse(data)

@login_required
def delete_hobby(request, hobby_pk):
    hobby = get_object_or_404(Hobby, pk=hobby_pk)
    if request.user == hobby.host:
        hobby.delete()
        return redirect("main")
    else:
        print('권한이 없습니다.')
        return redirect("hobby:detail", hobby_pk)