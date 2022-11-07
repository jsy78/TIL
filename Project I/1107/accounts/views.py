from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db.models import Prefetch
from django.core.paginator import Paginator
from articles.models import Article, Comment
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.


@require_safe
@login_required
def index(request):
    users = get_user_model().objects.order_by("-pk")
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def mypage(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    user_articles = (
        Article.objects.select_related("user").filter(user=user).order_by("-pk")
    )  # user.article_set.order_by("-pk")
    user_comments = (
        Comment.objects.select_related("user", "article")
        .filter(user=user)
        .order_by("-pk")
    )  # user.comment_set.order_by("-pk")
    like_articles = (
        get_user_model()
        .objects.prefetch_related(
            Prefetch("like_articles", queryset=Article.objects.select_related("user"))
        )
        .get(pk=request.user.pk)
        .like_articles.order_by("-pk")
    )  # user.like_articles.order_by("-pk")
    bookmark_articles = (
        get_user_model()
        .objects.prefetch_related(
            Prefetch(
                "bookmark_articles", queryset=Article.objects.select_related("user")
            )
        )
        .get(pk=request.user.pk)
        .bookmark_articles.order_by("-pk")
    )  # user.bookmark_articles.order_by("-pk")
    following_users = (
        get_user_model()
        .objects.prefetch_related(
            Prefetch("followings", queryset=get_user_model().objects.all())
        )
        .get(pk=request.user.pk)
        .followings.order_by("-pk")
    )  # user.bookmark_articles.order_by("-pk")

    user_articles_page = request.GET.get("user-articles-page", "1")
    user_comments_page = request.GET.get("user-comments-page", "1")
    like_articles_page = request.GET.get("like-articles-page", "1")
    bookmark_articles_page = request.GET.get("bookmark-articles-page", "1")
    following_users_page = request.GET.get("following-users-page", "1")
    # GET 방식으로 정보를 받아오는 데이터

    user_articles_paginator = Paginator(user_articles, "3")
    user_comments_paginator = Paginator(user_comments, "6")
    like_articles_paginator = Paginator(like_articles, "3")
    bookmark_articles_paginator = Paginator(bookmark_articles, "3")
    following_users_paginator = Paginator(following_users, "6")
    # Paginator(분할될 객체, 페이지 당 담길 객체 수)

    paginated_user_articles_lists = user_articles_paginator.get_page(user_articles_page)
    paginated_user_comments_lists = user_comments_paginator.get_page(user_comments_page)
    paginated_like_articles_lists = like_articles_paginator.get_page(like_articles_page)
    paginated_bookmark_articles_lists = bookmark_articles_paginator.get_page(
        bookmark_articles_page
    )
    paginated_following_users_lists = following_users_paginator.get_page(
        following_users_page
    )
    # 페이지 번호를 받아 해당 페이지를 리턴

    update_form = CustomUserChangeForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)

    context = {
        "user": user,
        "user_articles": user_articles,
        "user_comments": user_comments,
        "like_articles": like_articles,
        "bookmark_articles": bookmark_articles,
        "following_users": following_users,
        "paginated_user_articles_lists": paginated_user_articles_lists,
        "paginated_user_comments_lists": paginated_user_comments_lists,
        "paginated_like_articles_lists": paginated_like_articles_lists,
        "paginated_bookmark_articles_lists": paginated_bookmark_articles_lists,
        "paginated_following_users_lists": paginated_following_users_lists,
        "update_form": update_form,
        "password_form": password_form,
    }
    return render(request, "accounts/mypage.html", context)


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, "이미 로그인 중입니다.")
        return redirect("main")

    # POST 요청 처리
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # ModelForm의 save 메서드의 리턴값은 해당 모델의 인스턴스
            auth_login(request, user)  # 회원가입 직후 자동 로그인
            messages.success(request, "가입 성공")
            return redirect("main")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "이미 로그인 중입니다.")
        return redirect("main")

    if request.method == "POST":
        # AuthenticationForm은 ModelForm이 아님
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 form에서 인증된 유저 정보로 받을 수 있음
            auth_login(request, form.get_user())
            messages.success(request, "로그인 성공")
            return redirect(
                (request.GET.get("next") or request.POST.get("next")) or "main"
            )
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, "로그아웃 성공")
        return redirect("main")


@require_POST
def update(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "정보 수정 완료")
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
    else:
        messages.warning(request, "잘못된 접근입니다.")
    return redirect("accounts:mypage")


@require_POST
def password(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "비밀번호 변경 완료")
        else:
            messages.warning(request, "양식이 유효하지 않습니다.")
    else:
        messages.warning(request, "잘못된 접근입니다.")
    return redirect("accounts:mypage")


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    messages.success(request, "탈퇴 완료")
    return redirect("main")


@require_safe
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.user == user:
        return redirect("accounts:mypage")

    user_articles = (
        Article.objects.select_related("user").filter(user=user).order_by("-pk")
    )  # user.article_set.order_by("-pk")
    user_articles_page = request.GET.get("user-articles-page", "1")
    user_articles_paginator = Paginator(user_articles, "3")
    paginated_user_articles_lists = user_articles_paginator.get_page(user_articles_page)
    context = {
        "user": user,
        "user_articles": user_articles,
        "paginated_user_articles_lists": paginated_user_articles_lists,
    }
    return render(request, "accounts/profile.html", context)


@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), username=username)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                # if request.user in person.followers.all():
                person.followers.remove(request.user)
                is_followed = False
            else:
                person.followers.add(request.user)
                is_followed = True
            context = {
                "is_followed": is_followed,
                "followers_count": person.followers.count(),
                "followings_count": person.followings.count(),
            }
            return JsonResponse(context)
        return redirect("accounts:profile", person.username)
    return redirect("accounts:login")


@login_required
def followings(request):
    # user = get_object_or_404(get_user_model(), pk=request.user.pk)
    # users = (
    #     get_user_model()
    #     .objects.prefetch_related("followings")
    #     .get(pk=request.user.pk)
    #     .followings.order_by("-pk")
    # )
    # context = {
    #     "users": users,
    # }
    # return render(request, "accounts/followings.html", context)
    users = get_user_model().objects.prefetch_related(
        Prefetch(
            "followings",
            queryset=get_user_model().objects.prefetch_related("article_set").all(),
            to_attr="followings_users",
        )
    )
    articles = list()
    for followings_user in users.get(pk=request.user.pk).followings_users:
        for article in followings_user.article_set.all():
            articles.append(article)

    # articles = list()
    # for following_user in request.user.followings.all():
    #     for article in following_user.article_set.all():
    #         articles.append(article)

    articles.sort(key=lambda x: x.created_at, reverse=True)

    page = request.GET.get("page", "1")  # 페이지
    paginator = Paginator(articles, 5)
    page_list = paginator.get_page(page)
    context = {
        "articles": articles,
        "page_list": page_list,
    }
    return render(request, "accounts/followings.html", context)
