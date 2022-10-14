from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from reviews.models import Review

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect("main")
    # POST 요청 처리
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # ModelForm의 save 메서드의 리턴값은 해당 모델의 인스턴스
            auth_login(request, user)  # 회원가입 직후 자동로그인
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def index(request):
    users = get_user_model().objects.order_by("-pk")
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


@login_required
def mypage(request):
    user = request.user
    context = {"user": user}
    return render(request, "accounts/mypage.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect("main")
    if request.method == "POST":
        # AuthenticationForm은 ModelForm이 아님
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 form에서 인증된 유저 정보로 받을 수 있음
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:index")
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
    return redirect("accounts:index")


@login_required
def articles(request):
    reviews = Review.objects.filter(user=request.user).order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "accounts/articles.html", context)
