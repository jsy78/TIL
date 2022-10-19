# Django

## RDB

- RDB(관계형 데이터베이스) 복습
  - 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
  - RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본키라는 속성이 있음
  - 외래키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 표현할 수 있음
- RDB에서의 관계
  - 1:1
    - One-to-one relationships
    - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
  - 1:N
    - One-to-many relationships
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
    - 기준 테이블에 따라(1:N, One-to-many relationships)이라고도 함
  - M:N
    - Many-to-many relationships
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
    - 양쪽 모두에서 1:N 관계를 가짐

## Foreign Key

- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본키(Primary Key)를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
  - 이 때문에 참조하는 테이블의 행에는,  참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
  - 참조 무결성 : 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
    - 외래키가 선언된 테이블의 외래키 속성(열)의 값은 해당 테이블의 기본키 값으로 존재
- 외래키의 값이 반드시 부모 테이블의 기본키 일 필요는 없지만 유일한 값이어야 함

## Article - Comment (1:N)

### 기본 개념

- 게시판의 게시글과 1:N 관계를 나타낼 수 있는 댓글 구현
- 1:N 관계에서 게시글을 담당할 Article 모델은 1, 댓글을 담당할 Comment 모델은 N
  
  - "게시글은 댓글을 0개 이상 가진다."
    - "게시글(1)은 여러 개의 댓글(N)을 가진다."
    - "게시글(1)은 댓글을 가지지 않을 수도 있다."
  - "댓글은 반드시 하나의 게시글에 속한다."
  
- Article (1)

  | id (PK)    |
  | ---------- |
  | title      |
  | content    |
  | created_at |
  | updated_at |

- Comment (N)

  | id (PK)      |
  | ------------ |
  | content      |
  | created_at   |
  | updated_at   |
  | Article의 id |

- [ForeignKey(to, on_delete, **options)](https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey)

  - Django 모델에서 관계형 데이터베이스의 외래키 속성을 담당
  - 2개의 필수 인자가 필요
    - 참조하는 model class
    - on_delete 옵션
      - 외래키가 참조하는 객체가 사라졌을 때,  외래키를 가진 객체를 어떻게 처리할 지를 정의
      - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
      - PROTECT, SET_NULL, SET_DEFAULT … 등 여러 옵션 값들이 존재

### 모델 정의

```python
# articles/models.py

class Comment(models.Model):
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
    # 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성한다면 컬럼의 이름은 abcd_id가 되므로 관계 파악이 어려움
```

### 댓글 생성

```bash
$ python manage.py shell_plus
```

```shell
# Comment 클래스의 인스턴스 comment 생성
comment = Comment() 

# 인스턴스 변수 저장
comment.content = 'first comment'

# DB에 댓글 저장
comment.save()

# 에러 발생
django.db.utils.IntegrityError: NOT NULL constraint failed: articles_comment.article_id
# articles_comment 테이블의 ForeignKeyField, article_id 값이 저장시 누락되었기 때문
```

```shell
# 게시글 생성 및 확인
article = Article.objects.create(title='title', content='content')
article
=> <Article: title>

# 외래 키 데이터 입력
# 다음과 같이 article 객체 자체를 넣을 수 있음
comment.article = article
# 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래키 컬럼에 넣어 줄 수도 있지만 권장하지 않음

# DB에 댓글 저장 및 확인
comment.save()
comment
=> <Comment: first comment>
```

```shell
# 댓글 속성 값 확인
comment.pk 
=> 1

comment.content
=> 'first comment'

# 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
comment.article
=> <Article: title>

# article_pk는 존재하지 않는 필드이기 때문에 사용 불가, article_id로 사용해야 함
comment.article_id
=> 1
```

```shell
# 1번 댓글이 작성된 게시물의 pk 조회
comment.article.pk 
=> 1

# 1번 댓글이 작성된 게시물의 content 조회
comment.article.content
=> 'content'
```

```shell
# 두번째 댓글 작성하기
comment = Comment(content='second comment', article=article) 
comment.save()

comment.pk
=> 2

comment
=> <Comment: second comment>

comment.article_id
=> 1
```

### 관계 모델 참조

- [Related manager](https://docs.djangoproject.com/en/3.2/ref/models/relations/)
  - 1:N 혹은 M:N 관계에서 사용 가능한 문맥(context)
  - Django는 모델 간 1:N 혹은 M:N 관계가 설정되면 역참조할 때에 사용할 수 있는 manager를 생성

#### 역참조
- 나를 참조하는(나를 외래키로 지정한) 테이블을 참조하는 것
- 즉, 본인을 외래키로 참조 중인 다른 테이블에 접근하는 것
- 1:N 관계에서는 1이 N을 참조하는 상황
    - 외래 키를 가지지 않은 1이 외래키를 가진 N을 참조

```python
article = Article.objects.get(pk=1)

comments = article.comment_set.all()

for comment in comments:
    print(comment.content)
```

- Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
- article.comment 형식으로는 댓글 객체를 참조 할 수 없음
  - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음
- 대신 Django가 역참조 할 수 있는 manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음
  - 1:N 관계에서 생성되는 Related manger의 이름은 기본적으로 "참조하는\_모델명(소문자)_set" 이름 규칙으로 만들어짐
  - ForeignKey 클래스의 선택 옵션 중 하나인 related_name을 이용하면 역참조 시 사용하는 매니저 이름을 변경할 수 있음
- 반면 참조 상황(Comment -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능

### Comment 구현

#### CREATE

```python
# articles/forms.py
# 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article',)
```
```python
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
]
```

```python
# articles/views.py
# detail 페이지에서 CommentForm 출력 (view 함수)
# 외래키 입력 필드 article은 출력에서 제외

from .forms import ArticleForm, CommentForm
from .models import Article, Comment

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
        # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

```django
<!-- articles/detail.html -->
<!-- detail 페이지에서 CommentForm 출력 (템플릿) -->

{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% endblock content %}
```

#### READ

```python
# articles/views.py
# detail 페이지에서 작성한 댓글 목록 출력
# 특정 article에 있는 모든 댓글을 가져온 후 context에 추가

from .forms import ArticleForm, CommentForm
from .models import Article, Comment

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

```django
<!-- articles/detail.html -->
<!-- detail 템플릿에서 댓글 목록 출력하기 -->

{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
  </ul>
  <hr>
  ...
{% endblock content %}
```

#### DELETE

```python
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```

```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

```django
<!-- articles/detail.html -->
<!-- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력 -->

{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
    {% endfor %}
  </ul>
  <hr>
  ...
{% endblock content %}
```

#### 추가 구현

##### 댓글의 갯수

- DTL filter - length 사용

  ```django
  {{ comments|length }}
  
  {{ article.comment_set.all|length }}
  ```

- Queryset API - count() 사용

  ```django
  {{ comments.count }}
  
  {{ article.comment_set.count }}
  ```

```django
<!-- articles/detail.html -->
<h4>댓글 목록</h4>
{% if comments %}
  <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```

##### 댓글이 없는 경우

- DTL for empty 활용

```django
<!-- articles/detail.html -->

{% for comment in comments %}
  <li>
    {{ comment.content }}
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  </li>
{% empty %}
  <p>댓글이 없어요..</p>
{% endfor %}
```



