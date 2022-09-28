# Django

## App URL mapping

- 생성한 app의 view 함수가 많아지면 사용하는 path() 또한 많아지고,  app 또한 더 많이 작성됨

  - 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음

- 대안 1

  - 각 앱의 view 함수를 다른 이름으로 import하기

    ```python
    # firstpjt/urls.py
    
    from articles import views as articles_views
    from pages import views as pages_views
    
    urlpatterns = [
        ...,
        path('pages-index', pages_views.index),
    ]
    
    ```

- 대안 2

  - 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁

    ```python
    # pages/urls.py
    
    from django.urls import path
    from . import views
    
    urlpatterns = [
        
    ]
    ```

    ```python
    # articles/urls.py
    
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('index/', views.index),
        path('greeting/', views.greeting),
        path('dinner/', views.dinner),
        path('throw/', views.throw),
        path('catch/', views.catch),
        path('hello/<str:name>/', views.hello),
    ]
    ```

    ```python
    # firstpjt/urls.py
    
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
        path('pages/', include('pages.urls')),
        # urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있음
    ]
    ```

  - **include되는 앱의 url.py에 urlpatterns이 작성되어 있지 않다면 에러가 발생**

    -  pages 앱의 urlpatterns가 빈 리스트라도 작성되어 있어야 함

  - 대안 2로 수정을 거치면 메인 페이지의 주소가 변경됨

    - http://127.0.0.1:8000/index/ -> http://127.0.0.1:8000/articles/index/

### include()

- 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 돕는 함수
- 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라냄
- 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

### URL 구조의 변화

- 단일 앱의 URL을 project의 urls.py에서 관리

  ![https://ibb.co/wSLmQcs](https://i.ibb.co/dPcYpmg/1.png)

- 여러 앱의 URL을 project의 urls.py에서 관리

  ![https://ibb.co/BjTDk3h](https://i.ibb.co/jG3KtfC/2.png)

- 각각의 앱에서 URL을 관리

  ![https://ibb.co/k4n7hyx](https://i.ibb.co/7ncfGzX/3.png)

## URL namespace

```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
    # name 속성을 사용해 path에 별칭 설정 가능
]
```

```python
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # name 속성을 사용해 path에 별칭 설정 가능
]
```

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

```django
<!-- pages/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>pages 앱의 index</h1>
{% endblock content %}
```

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>
  <a href="{% url 'index' %}">pages 앱 index로 이동</a>
{% endblock content %}
```

- articles app index 페이지에 pages app index로 이동하는 하이퍼 링크를 작성 후 클릭 시 현재 페이지로 다시 이동하는 문제 발생
  - pages의 view name과 articles 앱의 view name이 index로 같아서 중복되기 때문
  - 각 앱의 urls.py 파일에 app_name attribute를 작성하여 URL namespace를 설정해주면 해결 가능
    - 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles' # namespace 적용
# app의 urls.py에 app_name을 명시

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
    # name 속성을 사용해 path에 별칭 설정 가능
]
```

```python
# pages/urls.py

from django.urls import path
from . import views

app_name = 'pages' # namespace 적용
# app의 urls.py에 app_name을 명시

urlpatterns = [
    path('index/', views.index, name='index'),
    # name 속성을 사용해 path에 별칭 설정 가능
]
```

```django
<!-- 템플릿에서 참조할 때는 다음과 같이 나타냄 -->
<a href="{% url 'articles:index' %}">articles의 index로 이동</a>
<a href="{% url 'pages:index' %}">pages의 index로 이동</a>
<!-- ":" 연산자를 사용하여 참조 -->
<!-- 예를 들어, app_name이 articles이고 URL name이 index인 주소 참조는 articles:index가 됨 -->
```

```django
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'articles:greeting' %}">greeting</a>
  <a href="{% url 'articles:dinner' %}">dinner</a>
  <a href="{% url 'articles:throw' %}">throw</a>
  <a href="{% url 'pages:index' %}">pages 앱 index로 이동</a>
{% endblock %}
```

```django
<!-- throw.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Throw</h1>
  <form action="{% url 'articles:catch' %}" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit" value="던져">
  </form>

  <a href="{% url 'articles:index' %}">뒤로</a>
{% endblock content %}
```

```django
<!-- catch.html -->

<a href="{% url 'articles:throw' %}">다시 던지러</a>
```

```django
<!-- greeting, dinner.html -->

<a href="{% url 'articles:index' %}">뒤로</a>
```

- app_name을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용해야 함
  - 그렇지 않으면 NoReverceMatch 에러가 발생

## Template namespace

- pages app의 index url (http://127.0.0.1:8000/pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력

  - Django는 기본적으로 app_name/templates/ 경로에 있는 템플릿 파일들만 찾을 수 있음

  - settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함

    ```python
    # settings.py
    
    TEMPLATES = [
        {
            ...,
            'APP_DIRS': True,
            # 바로 이 속성 값이 해당 경로를 활성화하고 있음
            ...
        },
    ]
    ```

- 디렉토리 생성을 통해 물리적으로 namespace 구분 필요

  - Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성, 폴더 구조를 app_name/templates/app_name/ 형태로 변경

  - Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것

    ```
    articles/
        templates/
            articles/
                index.html
                ...
                
    pages/
        templates/
            pages/
                index.html
                ...
    ```

- 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정

  ```python
  # articles/views.py
  
  def index(request):
      return render(request, 'articles/index.html')
  ```

  ```python
  # pages/views.py
  
  def index(request):
      return render(request, 'pages/index.html')
  ```

## DB ORM 활용

> 게시판 형식의 방명록을 간단히 구현해보자.

1. articles/models.py 작성

   ```python
   #articles/models.py
   
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       content = models.TextField()
   ```

2. migrate

   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```

3. articles/views.py 작성

   ```python
   # articles/views.py
   
   from django.shortcuts import render
   from .models import Article
   
   guestbook = []
   
   # Create your views here.
   def index(request):
       # DB에서 가져오기
       guestbook = Article.objects.all()
       context = {
           'guestbook': guestbook
       }
       return render(request, 'articles/index.html', context)
   
   def create(request):
       # DB에 저장
       Article.objects.create(content=request.GET.get('content'))
       context = {
           'content': content
       }
       return render(request, 'articles/create.html', context)
   ```

4. articles/template/article/create.html 작성

   ```django
   <!-- articles/template/article/create.html -->
   <!-- template namespace 적용 -->
   
   {% extends 'base.html' %}
   {% block content %}
   <body>
     <div>
       <h1>방명록</h1>
     </div>
     <div>
       <h2>글 목록</h2>
       {% for content in guestbook %}
       <p> {{ content.content }}</p>
       {% endfor %}
     </div>
     <div>
       <h2>글 작성</h2>
       <form action="/articles/create">
         <input type="text" name="content">
         <input type="submit">
       </form>
     </div>
   </body>
   {% endblock %}
   ```

   

