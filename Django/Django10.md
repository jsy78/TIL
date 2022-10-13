# Django

## 회원정보 수정

### UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

- UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일함

- UserChangeForm을 상속받아 커스텀한 CustomUserChangeForm을 사용

  - [UserCreationForm](./Django08.md)과 같이 ModelForm으로 구성되어 있으므로  User 모델 정보를 변경하여 활용해야 함

  ```python
  # accounts/forms.py
  
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserChangeForm
  
  class CustomUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm.Meta):
          model = get_user_model()
          fields = ('email', 'first_name', 'last_name',)
          # 상속 구조를 확인하고 수정하고자 하는 필드 작성 후 출력 변화 확인
  ```

### User model 상속 구조

1. UserChangeForm 클래스 구조 확인

   - Meta 클래스를 보면 User라는 model을 참조하는 ModelForm이라는 것을 확인할 수 있음

   - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147

2. User 클래스 구조 확인

   - 실제로 User 클래스는 Meta 클래스를 제외한 코드가 없고 AbstractUser 클래스를 상속 받고 있음
   - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405

3. AbstractUser 클래스 구조 확인

   - 클래스 변수명들을 확인해보면 회원수정 페이지에서 봤던 필드들과 일치한다는 것을 확인할 수 있음
   - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L334

4. 마지막으로 공식문서의 User 모델 Fields 확인

   - https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model

### 구현

```python
# accounts/urls.py

app_name = 'accounts'

urlpatterns = [
    ...,
    path('update/', views.update, name='update'),
]
```

```python
# accounts/views.py

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

```django
<!-- accounts/update.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

```django
<!-- base.html -->
<div class="container">
  <a href="{% url 'accounts:signup' %}">Signup</a>
  <a href="{% url 'accounts:update' %}">회원정보 수정</a>
  <hr>
  {% block content %}
  {% endblock content %}
</div>
```

## 비밀번호 변경

### PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form

- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함

- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 [SetPasswordForm](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L353)을 상속받는 서브 클래스

  ```python
  class SetPasswordForm(forms.Form):
      error_messages = {
          ...
      }
      new_password1 = forms.CharField(
          ...
      )
      new_password2 = forms.CharField(
          ...
      )
  
      def __init__(self, user, *args, **kwargs):
          ...

### 구현

```python
# accounts/urls.py

app_name = 'accounts'

urlpatterns = [
    ...,
    path('password/', views.change_password, name='change_password'),
]
```

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

```django
<!-- accounts/change_password.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>비밀번호 변경</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

- 변경 후 로그인 상태가 지속되지 못하는 문제 발생

### 세션 무효화 방지

- 비밀번호가 변경되면 기존 세션과 회원 인증 정보가 일치하지 않게 되므로 로그인 상태를 유지하지 못함
- **`update_session_auth_hash(request, user)`**
  - 현재 요청(current request)과 새 session data가 파생되어 업데이트된 사용자 객체를 가져오고, session data를 적절하게 업데이트해줌
  - 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

## 추가 정보

- AbstractBaseUser의 모든 subclass와 호환되는 forms

  - forms.ModelForm 상속
    - UserCreationForm
    - UserChangeForm
  - forms.Form 상속
    - AuthenticationForm
    - SetPasswordForm
    - PasswordChangeForm
    - AdminPasswordChangeForm

- 회원가입 이후 곧바로 로그인 진행하기

  ```python
  # accounts/views.py
  
  from django.contrib.auth import login as auth_login
  
  def signup(request):
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save() 
              auth_login(request, user) 
              return redirect('articles:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  ```

- 탈퇴하면서 세션 정보도 함께 제거

  ```python
  # accounts/views.py
  
  from django.contrib.auth import logout as auth_logout
  
  def delete(request):
      request.user.delete() # 1. 탈퇴 후
      auth_logout(request)  # 2. 로그아웃
  ```

  - "탈퇴 후, 로그아웃" 의 순서가 바뀌면 안됨
    - 로그아웃을 먼저 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어지기 때문

