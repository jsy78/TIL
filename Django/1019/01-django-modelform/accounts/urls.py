from django.urls import path
from . import views
# app_name은 왜 쓸까요?
# 우리는 기본적으로 URL을 모두 변수화해서 쓰고 있음
# Template, View에서 직접 '/accounts/' X 
# app_name과 path 이름으로 

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
]