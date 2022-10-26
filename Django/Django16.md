# Django

## Axios

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
  const URL = 'https://jsonplaceholder.typicode.com/todos/1'
  axios.get(URL)
    .then(res => console.log(res.data.title))
    .catch(err => console.log('Error!'))
</script> 
```

- 브라우저와 Node.js를 위한 Promise 기반의 클라이언트
- 확장 가능한 인터페이스와 함께 패키지로 사용이 간편한 라이브러리를 제공

### Promise

```javascript
const myPromise = axios.get(URL)

myPromise
  .then(response => {
    return response.data
  })

axios.get(URL)
  .then(response => {
    return response.data
  })
  .then(response => {
    return response.title
  })
  .catch(error => {
    console.log(error)
  })
  .finally(function () {
    console.log('나는 마지막에 무조건 시행!!!')
  })
```

- 비동기 작업을 관리하는 객체
  - 미래의 완료 또는 실패와 그 결과 값을 나타냄
  - 미래의 어떤 상황에 대한 약속
- 성공(이행)에 대한 약속 
  - .then(callback)
    - 이전 작업(promise)이 성공했을 때(이행됐을 때) 수행할 작업을 나타내는 callback 함수
    - 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
    - 따라서 성공했을 때의 코드를 callback 함수 안에 작성
- 실패(거절)에 대한 약속
  - .catch(callback)
    - .then이 하나라도 실패하면(거부되면) 동작 (동기식의 'try - except' 구문과 유사)
    -  이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음
- 무조건 시행되는 약속
  - .finally(callback)
    - Promise 객체를 반환
    - 결과와 상관없이 무조건 지정된 callback 함수가 실행
    - Promise가 성공되었는지 거절되었는지 판단할 수 없기 때문에 어떠한 인자도 전달받지 않음
    - 무조건 실행되어야 하는 절에서 활용, .then()과 .catch() 블록에서의 코드 중복을 방지
- 각각의 .then() 블록은 서로 다른 promise를 반환
  - .then()을 여러 개 사용(chaining)하여 연쇄적인 작업을 수행할 수 있음
  - 여러 비동기 작업을 차례대로 수행할 수 있음
- .then()과 .catch() 메소드는 모두 promise를 반환하기 때문에 chaining 가능
- callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
  - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
  - 비동기 작업이 성공하거나 실패한 뒤에 .then() 메소드를 이용한 경우도 마찬가지
- 주의
  - 반환 값이 반드시 있어야 함
  - 반환 값이 없다면 callback 함수가 이전의 promise 결과를 받을 수 없음

## 비동기 적용

### data-* attributes

```html
<div data-my-id="my-data"></div>
<script>
  const myId = event.target.dataset.myId
</script>

```

- 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환할 수 있는 방법
- 예를 들어 data-test-value 라는 이름의 특성을 지정했다면 JavaScript에서는 element.dataset.testValue로 접근할 수 있음
- 속성명 작성 시 주의사항
  - 대소문자 여부에 상관없이 xml로 시작하면 안 됨
  - 세미콜론을 포함해서는 안됨
  - 대문자를 포함해서는 안됨

### Follow

```django
<!-- base.html -->
<!-- 각각의 템플릿에서 script 코드를 작성하기 위한 block tag 영역 작성 -->

<body>
...
  {% block script %}
  {% endblock script %}
</body>
</html>
```

```python
# accounts/views.py

from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        me = request.user
        you = get_user_model().objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                # 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 JSON 응답
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
                # 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> / 
    팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
    <!-- 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성 -->
  </div>
  
  {% if request.user != person %}
    <form id="follow-form" data-user-id="{{ person.pk }}">
      <!-- form 요소 선택을 위해 id 속성 지정 및 선택 -->
      <!-- 불필요해진 action과 method 속성은 삭제 (요청은 axios로 대체되기 때문) -->
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  {% endif %}
  ...
{% endblock content %}

{% block script %}
  <!-- axios CDN 작성 -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const form = document.querySelector('#follow-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    // hidden 타입으로 숨겨져 있는 csrf 값을 가진 input 태그를 선택
    
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      // form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소
      const userId = event.target.dataset.userId
      axios({
        method: 'POST',
        url: `/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken}
        // https://docs.djangoproject.com/en/3.2/ref/csrf/#setting-the-token-on-the-ajax-request
      })
      .then((response) => {
        const isFollowed = response.data.is_followed
        const followBtn = document.querySelector('#follow-form > input[type=submit]')
                                 
        if (isFollowed === true) {
          followBtn.value = '언팔로우’
        } 
        else {
          followBtn.value = '팔로우’
        }
          
        const followersCountTag = document.querySelector('#followers-count')
        const followingsCountTag = document.querySelector('#followings-count')
        
        followersCountTag.innerText = response.data.followers_count
        followingsCountTag.innerText = response.data.followings_count
        // view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경
      })
      .catch((error) => {
        console.log(error.response)
      })
    })
  </script>
{% endblock script %}
```

### Like

```python
# articles/views.py
from django.http import JsonResponse

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False
        else:
            article.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

```django
<!-- articles/index.html -->
{% extends 'base.html' %}

{% block content %}
  ...
  {% for article in articles %}
    ...
    <div>
      <form class="like-forms" data-article-id="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
        {% else %}
          <input type="submit" value="좋아요" id="like-{{ article.pk }}">
        {% endif %}
      </form>
    </div>
    ...
  {% endfor %}
{% endblock content %}

{% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const forms = document.querySelectorAll('.like-forms')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    forms.forEach((form) => {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const articleId = event.target.dataset.articleId
        axios({
          method: 'POST',
          url: `/articles/${articleId}/likes/`,
          headers: {'X-CSRFToken': csrftoken},
        })
        .then((response) => {
          const isLiked = response.data.is_liked
          const likeBtn = document.querySelector(`#like-${articleId}`)
          if (isLiked === true) {
            likeBtn.value = '좋아요 취소'
          } 
          else {
            likeBtn.value = '좋아요'
          }
        })
        .catch((error) => {
          console.log(error.response)
        })
      })
    })
  </script>
{% endblock script %}
```





