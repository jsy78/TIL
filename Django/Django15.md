# Django

## Profile

```python
# accounts/urls.py

urlpatterns = [
    …
    path('profile/<username>/', views.profile, name='profile'),
]
```

```python
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    person = get_user_model().objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <hr>
  <h2>{{ person.username }}'s 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
  <hr>
  <h2>{{ person.username }}'s 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}
  <hr>
  <h2>{{ person.username }}'s 좋아요한 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
  <hr>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```

```django
<!-- base.html -->
<!-- Profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성 -->
...
<body>
  <div class="container">
    {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
...
```

```django
<!-- articles/index.html -->
...
<p>
  <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
</p>
...
```

## Follow (User-User M:N)

```python
# accounts/models.py
# ManyToManyField 작성 및 Migration 진행

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```python
# accounts/urls.py

urlpatterns = [
    ...,
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

```python
# accounts/views.py
# 데코레이터 및 is_authenticated 추가

from django.views.decorators.http import require_POST

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_user_model().objects.get(pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
          # if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
```

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    <div>
      팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in person.followers.all %}
            <input type="submit" value="Unfollow">
          {% else %}
            <input type="submit" value="Follow">
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
  ...
{% endblock content %}
```

## View decorators & functions

### Decorator

```python
def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('HIHI')
    return wrapper

@hello
def bye():
    print('byebye')
    
bye()

# 출력
# HIHI
# byebye
# HIHI
```

- 기존 함수를 수정하지 않고 기능을 추가해주는 wrapper 함수
- Django는 HTTP 처리를 위해 view 함수에 적용 할 수 있는 데코레이터를 제공

- `django.views.decorators.http`의 데코레이터를 사용

  - 요청 메소드를 기반으로 접근을 제한할 수 있음
  - 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
  - 메소드 목록
    - `require_http_methods()`
    - `require_POST()`
    - `require_safe()`

- View 함수가 특정한 요청 method만 허용하도록 하는 데코레이터

  ```python
  # views.py
  
  from django.views.decorators.http import require_http_methods
  
  @require_http_methods(['GET', 'POST'])
  def create(request):
      pass
  
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      pass
  ```

- View 함수가 POST 요청 method만 허용하도록 하는 데코레이터

  ```python
  # views.py
  # url로 delete를 시도하면 서버 로그에서 405 http status code를 확인할 수 있음
  # Method Not Allowed (GET): /articles/3/delete/
  # [04/Jan/2022 04:52:10] "GET /articles/3/delete/ HTTP/1.1" 405 0
  
  from django.views.decorators.http import require_http_methods, require_POST
  
  @require_POST
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('articles:index')
  ```

- View 함수가 GET 요청 method만 허용하도록 하는 데코레이터 (require_GET이 있지만 require_safe를 사용하는 걸 권장)

  ```python
  # views.py
  
  from django.views.decorators.http import require_http_methods, require_POST, require_safe
  
  @require_safe
  def index(request):
      ...
  
  @require_safe
  def detail(request, pk):
      ...
  ```

### @login_require와 require_POST

- 비로그인 상태로 detail 페이지에서 게시글 삭제를 시도하는 상황

  1. delete view 함수의 @login_required로 인해 로그인 페이지로 리다이렉트
     - `http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/`

  2. redirect로 이동한 로그인 페이지에서 로그인 진행
     - redirect는 반드시 GET 요청으로만 가능

  3. delete view 함수의 @require_POST로 인해 405 상태 코드를 받게 됨
     - 405(Method Not Allowed) status code 확인

- @login_required는 GET 요청을 처리하는 View 함수 에서만 사용해야 함

- POST method만 허용하는 delete같은 함수는 내부에서는 is_authenticated 속성 값을 사용해서 처리

  ```python
  # articles/views.py
  
  from django.views.decorators.http import require_POST
  
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = Article.objects.get(pk=pk)
          article.delete()
      return redirect('articles:login')
  ```

### Django Shortcut functions

- `get_object_or_404(klass, *args, **kwargs)`
  - 주어진 model manager에서 get()을 호출, 해당하는 객체가 존재하지 않을 경우 DoesNotExist 대신 404 상태코드를 발생시킴
- `get_list_or_404(klass, *args, **kwargs)`
  - 주어진 model manager에서 리스트로 변환된 filter()의 결과를 반환하고 결과 목록이 비어 있으면 404 상태코드를 발생시킴
