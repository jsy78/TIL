from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, CustomSocialForm
import requests, os
from hobby.models import Accepted
from community.models import Community
from products.models import Product

# Create your views here.

def signup(request):
    if request.method == "POST":
        secret = os.getenv('RECAPTCHA_SECRET_KEY')
        response = request.POST['captchatoken']
        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': secret, # 시크릿 키
            'response': response, # 토큰
        }
        res = requests.post(url, data=data)
        print(res.json()['success'])
        if not res.json()['success']:
            return JsonResponse({'result':res.json()['success']})
        else:
            form = CustomUserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)  # 로그인
                # 리다이렉트 URL
                return JsonResponse({'result':res.json()['success']})
            else:
                # 에러 발생
                messages.warning(request, '필수 정보를 입력해주세요.')
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)

# User.username json 데이터
def id_check(request):
    accounts = [i.username for i in get_user_model().objects.all()]
    data = {
        "accounts": accounts,
    }

    return JsonResponse(data)

# User.nickname json 데이터
def nickname_check(request):
    accounts = [i.nickname for i in get_user_model().objects.all()]
    data = {"accounts": accounts}
    return JsonResponse(data)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect('main')
    
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect((request.GET.get("next") or request.POST.get("next")) or "main")
            else:
                # 에러 발생
                messages.warning(request, '아이디 또는 비밀번호를 잘못 입력했습니다.')
        else:
            form = AuthenticationForm()

        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    # 로그아웃 메시지
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect("accounts:login")


@login_required
def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)

    
    my_Product = Product.objects.filter(user=user).order_by('-id')
    my_community = Community.objects.filter(user=user).order_by('-id')
    
    # 정렬할 테이블 -pk 포멧
    # recently_like = '-{}.id'.format(Community.like.through._meta.db_table)
    # a = Community.objects.filter(like=user).order_by(recently_like)

    like_community = user.like_community.all().order_by("-community_community_like.id")
    like_product = user.like_product.all().order_by("-products_product_like_users.id")

    blockers = request.user.blocking.all()
    accepted = Accepted.objects.filter(user=user, joined=True).order_by('-id')
    waiting = Accepted.objects.filter(user=user, joined=False).order_by('-id')
    print(waiting)

    context = {
        "user": user,
        "accepted" : accepted,
        "waiting" : waiting,
        "blockers" : blockers,
        "my_product" : my_Product,
        "my_community": my_community,
        "like_community" : like_community,
        "like_product": like_product,
    }
    
    return render(request, "accounts/detail.html", context)


@login_required
def follow(request, pk):
    accounts = get_object_or_404(get_user_model(), pk=pk)
    if request.user == accounts:
        return redirect("accounts:detail", pk)
    if request.user in accounts.followers.all():
        accounts.followers.remove(request.user)
        accounts.save()
    else:
        accounts.followers.add(request.user)
        accounts.save()
    # 상세 페이지로 redirect
    return redirect("accounts:detail", pk)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("main")


@login_required
def update(request, pk):
    user_info = get_object_or_404(get_user_model(), pk=pk)
    # 요청한 유저가 로그인한 해당 유저인 경우
    if request.method == "POST":
        user_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        # 유저폼 유효성 확인
        if user_form.is_valid():
            user_form.save()
            return redirect("accounts:detail", user_info.pk)
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    context = {
        "user_form": user_form,
        "user_info": user_info,
    }
    return render(request, "accounts/update.html", context)


@login_required
def password_change(request, pk):
    user_info = get_object_or_404(get_user_model(), pk=pk)

    if request.method == 'POST':
        # django에서 지원하는 패스워드 체인지폼
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            return redirect("accounts:detail", user_info.pk)
    else:
        form = CustomPasswordChangeForm(request.user)

    context = {
        "form": form,
    }
    return render(request, 'accounts/password.html', context)

def kakao_login(request):
    # API KEY 
    app_key = os.getenv("KAKAO_REST_API_KEY")
    # callback 받을 url  
    # redirect_uri = 'http://localhost:8000/accounts/login/kakao/callback'
    redirect_uri = 'http://mohobby-env.eba-v2kvw9tu.ap-northeast-2.elasticbeanstalk.com/accounts/login/kakao/callback'
    # 카카오 로그인 URL
    kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'

    return redirect(
        # 서버의 정보를 카카오 로그인 페이지에 전송하게된다.
        f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}'
    )



def KakaoCallBack(request):
    # 카카오에서 callback 받음 
    auth_code = request.GET.get('code')
    kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    data = {
        # OAuth 인증
        'grant_type': 'authorization_code',
        # 카카오 API KEY
        'client_id': os.getenv("KAKAO_REST_API_KEY"),
        'redirection_uri': 'http://mohobby-env.eba-v2kvw9tu.ap-northeast-2.elasticbeanstalk.com/accounts/login/kakao/callback',
        'code': auth_code,
    }
    # 토큰 발급받기
    token_response = requests.post(kakao_token_api, data=data)
    
    # 발급받은 토큰 가공
    access_token = token_response.json().get('access_token')
    user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})

    # json 파일로 카카오 계정 정보 받아오기
    kakao_user_data = user_info_response.json()
    # 일단 닉네임만. 받을 수 있는 개인정보는 설정으로 바꿀수있음.
    kakao_user_id = kakao_user_data['id']
    
    if get_user_model().objects.filter(kakao_id=kakao_user_id).exists():
        kakao_user = get_user_model().objects.get(kakao_id=kakao_user_id)
        auth_login(request, kakao_user)
        return redirect(request.GET.get("next") or "main")
    else:
        kakao_login_user = get_user_model()()
        kakao_login_user.kakao_id = kakao_user_id
        kakao_login_user.username = kakao_user_id
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(kakao_id=kakao_user_id)
    
        auth_login(request, kakao_user)
        return redirect("accounts:social_signup", kakao_user.pk)

@login_required 
def social_signup(request, pk):
    user_info = get_user_model().objects.get(pk=pk)
    # 로그인한 유저가 찾는 유저가 맞는지 확인
    if request.user == user_info:
        if request.method == "POST":
            secret = os.getenv('RECAPTCHA_SECRET_KEY')
            response = request.POST['captchatoken']
            url = 'https://www.google.com/recaptcha/api/siteverify'
            data = {
                'secret': secret, # 시크릿 키
                'response': response, # 토큰
            }
            res = requests.post(url, data=data)
            print(res.json()['success'])
            if not res.json()['success']:
                return JsonResponse({'result':res.json()['success']})
            else:
                # 소셜 폼 사용
                form = CustomSocialForm(request.POST, request.FILES, instance=request.user)
                if form.is_valid():
                    form.save()
                    return JsonResponse({'result':res.json()['success']}) 
                else:
                    # 필수 정보를 입력하지 않았을 때 출력하는 에러메시지 
                    messages.warning(request, '필수 정보를 입력해주세요.')
        else:
            form = CustomSocialForm(instance=request.user)
    
    context = {
        "form": form,
        "user_info": user_info,
    }
    return render(request, 'accounts/social_signup.html', context)

# 차단
@login_required
def block(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if user != request.user:
        if user.blockers.filter(pk=request.user.pk).exists():
            user.blockers.remove(request.user)
            user.save()
        else:
            user.blockers.add(request.user)
            user.save()
    return redirect("accounts:detail", request.user.pk)
