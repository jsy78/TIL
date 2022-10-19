# Django

## User - Comment (1:N)

### 기본 개념

- 유저와 1:N 관계를 나타낼 수 있는 댓글 구현

- 1:N 관계에서 User 모델은 1, Comment 모델은 N
  
  - "0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음"
  
- User (1)

  | id (PK)    |
  | ---------- |
  | username   |
  | first_name |
  | last_name  |
  | ...        |

- Comment (N)

  | id (PK)    |
  | ---------- |
  | content    |
  | created_at |
  | updated_at |
  | User의 id  |

### 모델 정의

```python
# articles/models.py

from django.conf import settings

class Comment(models.Model):
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

### Comment 구현

#### CREATE

```python
# articles/forms.py
# 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성
# create 템플릿에서 외래키 입력 필드(article, user) 제거

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'user',)
```
```python
# articles/views.py
# detail 페이지에서 CommentForm 출력 (view 함수)

from .forms import ArticleForm, CommentForm
from .models import Article, Comment

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
        # https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)
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
<!-- detail 템플릿에서 댓글 목록, 각 댓글의 작성자 출력하기 -->

{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.user }} - {{ comment.content }}</li>
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
# 본인의 댓글만 삭제 할 수 있도록

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

```django
<!-- articles/detail.html -->
<!-- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력 -->
<!-- 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함 -->

{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'articles:index' %}">back</a>
  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.user }} - {{ comment.content }}
        {% if request.user == comment.user %}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
  <hr>
  ...
{% endblock content %}
```

