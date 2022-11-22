from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomAuthenticationForm,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, "이미 로그인 중입니다.")
        return redirect("main")

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
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "main")
    else:
        form = CustomAuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@require_safe
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    like_articles = user.like_articles.all()
    bookmark_articles = user.bookmark_articles.all()
    following_users = user.followings.all()
    follower_users = user.followers.all()
    context = {
        "user": user,
        "like_articles": like_articles,
        "bookmark_articles": bookmark_articles,
        "following_users": following_users,
        "follower_users": follower_users,
    }
    return render(request, "accounts/profile.html", context)


@require_POST
def follow(request, username):
    if not request.user.is_authenticated:
        messages.warning(request, "로그인이 필요합니다.")
        return redirect("accounts:login")

    user = get_object_or_404(get_user_model(), username=username)
    if user != request.user:
        if user.followers.filter(username=request.user.username).exists():
            user.followers.remove(request.user)
            is_followed = False
        else:
            user.followers.add(request.user)
            is_followed = True
        context = {
            "is_followed": is_followed,
            "followersCount": user.followers.all().count(),
            "followingsCount": user.followings.all().count(),
        }
        return JsonResponse(context)
    return redirect("accounts:profile", user.username)


@login_required
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필 정보가 성공적으로 변경되었습니다.")
            return redirect("accounts:profile", request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "비밀번호 변경이 성공적으로 완료되었습니다.")
            return redirect("accounts:login")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password.html", context)


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, "로그아웃 완료")
    return redirect("main")


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    messages.success(request, "탈퇴 완료")
    return redirect("main")
