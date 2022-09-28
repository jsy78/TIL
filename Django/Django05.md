# Django

## Naming  URL patterns

> 만약 "index/"의 문자열 주소를 "new-index/"로 바꿔야 한다고 가정해보자
>
> 그렇다면 "index/" 주소를 사용했던 모든 곳을 찾아서 변경해야 하는 번거로움이 발생함

- 링크에 URL을 직접 작성하지 않고 "path()" 함수에 name 속성을 추가
  - DTL의 Tag 중 하나인 URL 태그를 사용해서 "path()" 함수에 작성한 name을 사용할 수 있음
- URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
- Django는 URL에 이름을 지정하는 방법을 제공함
  - view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

```python
# articles/urls.py

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
```

### Built-in tag - "url"

```django
{% url '' %}
```

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법

```django
<!-- catch.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Catch</h1>
  <h2>여기서 {{ message }}를 받았어!!</h2>
  <a href="{% url 'throw' %}">다시 던지러</a>
{% endblock content %}
```

```django
<!-- throw.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Throw</h1>
  <form action="{% url 'catch' %}" method="GET">
    ...
  </form>

  <a href="{% url 'index' %}">뒤로</a>
{% endblock content %}
```

```django
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock content %}

<!-- dinner, greeting.html-->

<a href="{% url 'index' %}">뒤로</a>
```

#### DRY 원칙

- Don’t Repeat Yourself
- 소스 코드에서 동일한 코드를 반복하지 말자는 의미
- 동일한 코드가 반복된다면 잠재적인 버그의 위협이 증가함
- 반복되는 코드를 변경해야 하는 경우, 반복되는 모든 코드를 찾아서 수정해야 함
- 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐

## Model

![https://ibb.co/YtXpH1x](https://i.ibb.co/30vBgjn/1.png)

- Django는 Model을 통해 데이터에 접근하고 조작, 관리함
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조 (layout)
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 대응 됨(mapping)
  - 모델 클래스 1개 === 데이터베이스 테이블 1개

### Model 작성

- 새 프로젝트(crud), 앱(articles) 작성 및 앱 등록

  ```bash
  $ django-admin startproject crud .
  
  $ python manage.py startapp articles
  ```

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      'articles',
      ...
  ]
  ```

- models.py 작성 및 분석

  - 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것
  - 모델 클래스 === 테이블 스키마

  ```python
  # articles/models.py
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- 각 모델은 `django.models.Model` 클래스의 서브 클래스

  - 즉, 각 모델은 `django.db.models` 모듈의 Model 클래스를 상속받아 구성됨
  - 클래스 상속 기반 형태의 Django 프레임워크 개발

- models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의

  - Article에는 어떤 데이터 구조가 필요한지 정의
  - 클래스 변수 title과 content, created_at, updated_at은 DB 필드를 나타냄

- 클래스 변수 (속성)명은 DB 필드의 이름을 의미

- 클래스 변수 값 (models 모듈의 Field 클래스)은 DB 필드의 데이터 타입을 의미

  - **`CharField(max_length=None, **options)`**
    - 길이의 제한이 있는 문자열을 넣을 때 사용
    - `max_length`
      - 필드의 최대 길이(문자)
      - CharField의 필수 인자
      - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용됨
  - **`TextField(**options)`**
    - 글자의 수가 많을 때 사용
    - max_length 옵션 작성 시 사용자 입력 단계에서는 반영 되지만, 모델과 데이터베이스 단계에는 적용되지 않음
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음
  - **`DateTimeField(**options)`**
    - Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
    - DateField를 상속받는 클래스
    - `auto_now_add`
      - 최초 생성 일자 (Useful for creation of timestamps)
      - 데이터가 실제로 만들어질 때 현재 날짜와 시간으로 자동으로 초기화 되도록 함
    - `auto_now`
      - 최종 수정 일자 (Useful for “last-modified” timestamps)
      - 데이터가 수정될 때마다 현재 날짜와 시간으로 자동으로 갱신되도록 함
  - Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형 (INT, TEXT 등)을 정의
  - 데이터 유형에 따라 다양한 모델 필드를 제공
    - `DataField()`, `CharField()`, `IntegerField()` 등
    - [Model field reference | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

### Migrations

```bash
$ python manage.py makemigrations
```

- 모델의 변경사항에 대한 새로운 migration을 만들 때 사용

```bash
$ python manage.py migrate
```

- makemigrations로 만든 설계도를 실제 데이터베이스(db.sqlite3)에 반영하는 과정
- 모델의 변경사항과 데이터베이스를 동기화

```bash
$ python manage.py showmigrations
```

- migrations 파일들의 migrate 여부를 확인하는 용도
- `[X]` 표시가 있으면 migrate가 완료되었음을 의미

```bash
$ python manage.py sqlmigrate articles 0001
```

- 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인 할 수 있음

## ORM

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 (Django <-> DB)데이터를 변환하는 기술
- SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
- 객체 지향적 접근으로 인한 높은 생산성
- 단, ORM 만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 있음

### QuerySet API

| Article     | .objects | .all()       |
| :---------- | :------- | :----------- |
| Model class | Manager  | QuerySet API |

- Objects manager
  - Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스
  - Django는 기본적으로 모든 Django 모델 클래스에 대해 objects 라는 Manager 객체를 자동으로 추가함

- QuerySet
  - 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
    - 순회가 가능한 데이터로, 1개 이상의 데이터를 불러와 사용할 수 있음
    - 단, 데이터베이스가 단일 객체를 반환 할 때는 QuerytSet이 아닌 모델(Class)의 인스턴스로 반환됨
  - Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음

#### CREATE

```python
article = Article()
# 클래스를 통한 인스턴스 생성

article.title = 'first'
article.content = 'django!' 
# 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

article.save()
# 인스턴스로 save 메서드 호출
```

또는,

```python
Article.objects.create(title='third', content='django!')
# create() 메소드 활용
```

#### READ

- all()

```shell
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
# 전체 데이터 조회
```

- get()

```shell
>>> Article.objects.get(pk=1)
<Article: Article object (1)>
# 단일 데이터 조회
# primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용

>>> Article.objects.get(pk=100)
DoesNotExist: Article matching query does not exist.
# 객체를 찾을 수 없으면 DoesNotExist 예외 발생

>>> Article.objects.get(content='django!')
MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
# 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외 발생
```

- filter()

```shell
>>> Article.objects.filter(content='django!')
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
# 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

>>> Article.objects.filter(title='ssafy')
<QuerySet []>
# 조회된 객체가 없어도 QuerySet을 반환

>>> Article.objects.filter(title='first')
<QuerySet [<Article: Article object (1)>]>
# 조회된 객체가 1개여도 QuerySet을 반환
```

- Field lookups
  - [0825 - Database 강의](../Database/Database08.md)
  - [QuerySet API reference | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)

#### UPDATE

```shell
>>> article = Article.objects.get(pk=1)
# 인스턴스 객체 조회

>>> article.title = 'byebye'
# 인스턴스 변수를 변경

>>> article.save()
# 저장

>>> article.title
'byebye'
# 정상적으로 변경된 것을 확인
```

#### DELETE

```shell
>>> article = Article.objects.get(pk=1)
# 인스턴스 객체 조회

>>> article.delete()
(1, {'articles.Article': 1})
# delete 메서드 호출

>>> Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist.
# 1번 데이터는 이제 조회할 수 없음
```

## HTTP request method

- [0926 - Django 강의](../Django/Django03.md)

### GET

- 특정 리소스를 가져오도록 요청할 때 사용
- 반드시 데이터를 가져올 때만 사용해야 함
- DB에 변화를 주지 않음
- CRUD에서 R 역할을 담당
- 검색에서 GET을 사용하는 이유는?
  - 검색은 서버에 영향을 미치는 것이 아닌 특정 데이터를 조회만 하는 요청이기 때문
  - 특정 페이지를 조회하는 요청을 보내는 HTML의 a tag 또한 GET을 사용

### POST

- 서버로 데이터를 전송할 때 사용
- 서버에 변경사항을 만듦
- 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
- GET의 쿼리 스트링 파라미터와 다르게 URL로 데이터를 보내지 않음
- CRUD에서 C/U/D 역할을 담당

```django
<!-- templates/articles/new.html -->
<!-- URL에서 쿼리 스트링 파라미터가 없어진 것을 확인해보기 -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    ...
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

```python
def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content') 
    # POST 메소드로 전송된 데이터를 받아오기 위해서는 위와 같이 수정 필요
    
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')
```

## CSRF

- Cross-Site-Request-Forgery
- "사이트 간 요청 위조"
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

### CSRF 공격 방어

- Security Token 사용 방식 (CSRF Token)

  - 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
  - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
  - 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용
  - Django는 DTL에서 csrf_token 템플릿 태그를 제공

- csrf_token 템플릿 태그

  `{% csrf_token %}`

  ```django
  <!-- templates/articles/new.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      ...
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock content %}
  ```

  - csrf_token 은 해당 POST 요청이 내가 보낸 것인지를 검증하는 것
  - 해당 태그가 없다면 Django 서버는 요청에 대해 403 forbidden으로 응답
  - 템플릿에서 **내부** URL로 향하는 POST form을 쓸 경우에 사용
    - 외부 URL로 향하는 POST form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기 때문에 사용해서는 안됨

## CRUD with  view functions

### 사전 준비

1. base 템플릿 작성
   - bootstrap CDN 및 템플릿 추가 경로 작성

```django
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- bootstrap CSS CDN -->
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock content %}
  </div>
  <!-- bootstrap JS CDN -->
</body>
</html>
```

```python
# settings.py

TEMPLATES = [
    {
        ...,
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        ...
    }
]
```

2. url 분리 및 연결

```python
# articles/urls.py

from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
]
```

```python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

```python
# articles/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
{% endblock content %}
```

### CREATE

- CREATE 로직을 구현하기 위해 필요한 view 함수
  - 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개
    - "new" view function
  - 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수 1개
    - "create" view function

```python
# articles/urls.py

from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
```

```python
# articles/views.py

from django.shortcuts import render, redirect

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content')
    
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 2.
    article = Article(title=title, content=content)
    article.save()
    
    # 3. 
    # Article.objects.create(title=title, content=content)
    
    return redirect('articles:index')
	# return redirect('/articles/')
	# 게시글 작성 후 메인 index 페이지로 돌아가도록 함
```

```django
<!-- templates/articles/new.html -->
<!-- 글쓰기 페이지 -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    <!-- DB에 영향을 미치기 때문에 POST method를 사용 -->
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
  <!-- 메인 index 페이지로 이동할 수 있는 하이퍼 링크 작성 -->
{% endblock content %}
```

```django
<!-- templates/articles/create.html -->
<!-- 게시글 작성 후 확인하기 위한 임시 페이지 -->
<!-- 잘 작동함을 확인하면 삭제 -->

{% extends 'base.html' %}

{% block content %}
  <h1>성공적으로 글이 작성되었습니다.</h1>
{% endblock content %}
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:new' %}">NEW</a>
  <!-- 글쓰기 페이지로 이동할 수 있는 하이퍼 링크 작성 -->
  <hr>
  ...
{% endblock content %}
```

### READ 1 (index page)

- index 페이지는 전체 게시글을 조회해서 출력함

```python
# articles/views.py

from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

```django
<!--templates/articles/index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:new' %}">NEW</a>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
{% endblock content %}
```

### READ 2 (detail page)

- 개별 게시글 상세 페이지 제작
- 모든 게시글 마다 뷰 함수와 템플릿 파일을 만들 수는 없음
  - 글의 번호인 pk (id)를 활용해서 하나의 뷰 함수와 템플릿 파일로 대응
- Variable Routing 활용

```python
# articles/urls.py

urlpatterns = [
    ...
    path('<int:pk>/', views.detail, name='detail'),
    # URL로 특정 게시글을 조회할 수 있는 번호를 받음
]
```

```python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
                                 # 오른쪽 pk는 variable routing을 통해 받은 pk
                                 # 왼쪽 pk는 DB에 저장된 레코드의 id 컬럼
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

```django
<!-- templates/articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

```django
<!--templates/articles/index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:new' %}">NEW</a>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
	<a href="{% url 'articles:detail' article.pk %}">detail</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

```python
# articles/views.py

def create(request):
    ...
    return redirect('articles:detail', article.pk)
	# redirect 인자 변경
    # 게시글 작성 후 해당 게시글 상세 페이지로 돌아가도록 함
```

### DELETE

- 모든 글을 삭제하는 것이 아니라 삭제하고자 하는 특정 글을 조회 후 삭제해야 함

```python
# articles/urls.py

urlpatterns = [
    ...
    path('<int:pk>/delete/', views.delete, name='delete'),
```

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    
    return redirect('articles:index')
```

```django
<!-- templates/articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    <!-- DB에 영향을 미치기 때문에 POST method를 사용 -->
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```