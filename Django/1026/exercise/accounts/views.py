from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
@require_safe
def index(request):
    users = get_user_model().objects.order_by("-pk")
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


@require_safe
def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, "이미 로그인 중입니다.")
        return redirect("main")

    # POST 요청 처리
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
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


@require_http_methods(['GET', 'POST'])
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
            return redirect((request.GET.get("next") or request.POST.get("next")) or "main")
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


@require_safe
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    context = {
        "user": user,
    }
    return render(request, "accounts/profile.html", context)


@require_safe
def article(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles = user.article_set.order_by("-pk")
    context = {
        "user": user,
        "articles": articles,
    }
    return render(request, "accounts/article.html", context)


@require_safe
def comment(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    comments = user.comment_set.order_by("-pk")
    context = {
        "user": user,
        "comments": comments,
    }
    return render(request, "accounts/comment.html", context)


@require_safe
def like_article(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles = user.like_articles.order_by("-pk")
    context = {
        "user": user,
        "articles": articles,
    }
    return render(request, "accounts/like_article.html", context)


@require_safe
def like_comment(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    comments = user.like_comments.order_by("-pk")
    context = {
        "user": user,
        "comments": comments,
    }
    return render(request, "accounts/like_comment.html", context)


@require_POST
def follow(request, pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=pk)
        if person != request.user :
            if person.followers.filter(pk=request.user.pk).exists():
          # if request.user in person.followers.all():
                person.followers.remove(request.user)
                is_followed = False
            else:
                person.followers.add(request.user)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': person.followers.count(),
                'followings_count': person.followings.count(),
            }
            return JsonResponse(context)
        return redirect("accounts:profile", person.username)
    return redirect('accounts:login')     


@require_safe
def following(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    users = user.followings.order_by("-pk")
    context = {
        "user": user,
        "users": users,
    }
    return render(request, "accounts/following.html", context)


@require_safe
def follower(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    users = user.followers.order_by("-pk")
    context = {
        "user": user,
        "users": users,
    }
    return render(request, "accounts/follower.html", context)    


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "정보 수정 성공")
            return redirect("accounts:profile", request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
@require_http_methods(['GET', 'POST'])
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "비밀번호 변경 성공")
            return redirect("accounts:profile", request.user.username)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password.html", context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    messages.success(request, "탈퇴 완료")
    return redirect("main")
