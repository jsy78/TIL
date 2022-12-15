from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/follow/", views.follow, name="follow"),
    path("delete/", views.delete, name="delete"),
    path("update/<int:pk>/", views.update, name="update"),
    
    # unique값 체크 url
    path("id_check/", views.id_check, name="id_check"),
    path("nickname_check/", views.nickname_check, name="nickname_check"),
    
    # 비밀번호 변경
    path("password_change/<int:pk>/", views.password_change, name="password_change"),
    
    # 카카오 로그인
    path("login/kakao/", views.kakao_login, name="kakao_login"),
    path("login/kakao/callback/", views.KakaoCallBack),

    # 소셜 로그인 폼
    path("social_signup/<int:pk>", views.social_signup, name="social_signup"),
    
    # 회원 차단
    path("<int:pk>/block", views.block, name="block"),
]
