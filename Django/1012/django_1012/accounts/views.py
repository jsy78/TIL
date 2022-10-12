from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model  # from .models import User

# Create your views here.
@login_required
def index(request):
    users = get_user_model().objects.order_by("-pk")
    context = {"users": users}
    return render(request, "accounts/index.html", context)


@login_required
def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('mains:index')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "mains:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("mains:index")
