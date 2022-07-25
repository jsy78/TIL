# API

- Application Programming Interface
- 컴퓨터나 컴퓨터 프로그램 사이의 연결
- 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공
- 사용하는 방법을 기술하는 문서나 표준 은 API 사양/명세 (specification)

## API 사용 전에 확인해야 할 것

| 요청(Request)<br/>(정보를 원하는 사람) | 주소(URL)<br/>----------><br/><----------<br/>문서(JSON) | 응답(Response)<br/>(정보를 주는 사람) |
| :------------------------------------: | :------------------------------------------------------: | :-----------------------------------: |

- 요청하는 방식에 대한 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하는 기능에 대한 추가 경로
    - 요청 변수 (필수와 선택)

- 응답 결과에 대한 이해
  - 응답 결과 타입(JSON)
  - 응답 결과 구조

## Request

- [Python Requests](https://requests.readthedocs.io/en/latest/)

- HTTP 요청에 따라 사용하는 함수가 다름

  - GET 방식: `requests.get()`
  - POST 방식: `requests.post()`
  - PUT 방식: `requests.put()`
  - DELETE 방식: `requests.delete()`

- 응답 상태 확인

  - `response.status_code`
  - [requests/status_codes.py at main · psf/requests (github.com)](https://github.com/psf/requests/blob/main/requests/status_codes.py)

- 응답 전문 확인

  - `response.content` : 바이너리 타입
  - `response.text` : 문자열 타입
  - `response.json()` : json 응답일 경우 파이썬 자료형으로 변환

- 응답 헤더

  - 응답에 대한 메타 데이터를 담고 있음
  - `headers` 속성을 통해 딕셔너리의 형태로 얻을 수 있음

- 요청 쿼리

  - GET 방식으로 HTTP 요청을 할 경우 쿼리 스트링을 통해 응답받을 데이터를 필터링하는 경우가 많음

  - `params` 옵션을 사용하면 쿼리 스트링을 딕셔너리 형태로 넘길 수 있음

    ```python
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('https://httpbin.org/get', params=payload)
    ```

- 요청 전문

  - POST나 PUT 방식으로 HTTP 요청을 할 경우 보통 요청 전문(request body/payload)에 데이터를 담아서 보냄
  - `data` 옵션을 사용하면, HTML 양식(form)의 데이터를 전송할 수 있음
    -  `Content-Type` 요청 헤더는 `application/x-www-form-urlencoded`로 자동 설정됨
  - `json` 옵션을 사용하면, REST API로 JSON 포멧의 데이터를 전송할 수 있음
    - `Content-Type` 요청 헤더는 `application/json`로 자동 설정됨

- 요청 헤더

  - `headers` 옵션을 사용하면 요청 헤더를 직접 설정할 수 있음
    - 인증 토큰을 보낼 때 유용하게 사용 가능함

## API 활용 예시

- [bithumb API Docs](https://apidocs.bithumb.com/reference)
- [The Movie Database API](https://developers.themoviedb.org/3)

```python
# pip install requests 
import requests
from pprint import pprint
# URL로
order_currency = 'BTC' 
payment_currency = 'KRW' 
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)
# 응답 받은 값을 가져온다.
print(response, type(response)) 
# <Response [200]> <class 'requests.models.Response'>

# 속성 예시
print(response.status_code) 
# 200 
print(response.text, type(response.text)) 
'''
{"status":"0000","data":{"opening_price":"29813000","closing_price":"30564000","min_price":"29738000","max_price":"30680000","units_traded":"3972.53311863","acc_trade_value":"120592237789.8685","prev_closing_price":"29812000","units_traded_24H":"5875.84817743","acc_trade_value_24H":"177744906151.7639","fluctate_24H":"341000","fluctate_rate_24H":"1.13","date":"1658477852565"}} <class 'str'>
''' 

# 메소드 예시
# .json() 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경!
pprint(response.json())
'''
{'data': {'acc_trade_value': '120592237789.8685',
          'acc_trade_value_24H': '177744906151.7639',
          'closing_price': '30564000',
          'date': '1658477852565',
          'fluctate_24H': '341000',
          'fluctate_rate_24H': '1.13',
          'max_price': '30680000',
          'min_price': '29738000',
          'opening_price': '29813000',
          'prev_closing_price': '29812000',
          'units_traded': '3972.53311863',
          'units_traded_24H': '5875.84817743'},
 'status': '0000'}
'''
print(type(response.json())) 
# <class 'dict'>

data = response.json()
# data는 딕셔너리 => key로 접근
print(data.get('data').get('closing_price'))
# 30564000
```

```python
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/43261'

params = {
    'api_key': '', # 발급받은 api key값 입력
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
pprint(response)

'''
{'adult': False,
 'backdrop_path': None,
 'belongs_to_collection': None,
 'budget': 0,
 'genres': [{'id': 18, 'name': '드라마'}, {'id': 10402, 'name': '음악'}],
 'homepage': '',
 'id': 43261,
 'imdb_id': 'tt0047873',
 'original_language': 'en',
 'original_title': 'The Benny Goodman Story',
 'overview': '',
 'popularity': 1.397,
 'poster_path': '/pbxZjnYn2hcwHb4Vr20wu0k2HYa.jpg',
 'production_companies': [{'id': 10330,
                           'logo_path': '/nY62adzeba5GVK8LJYD6yd9R8H4.png',
                           'name': 'Universal International Pictures',
                           'origin_country': ''}],
 'production_countries': [{'iso_3166_1': 'US',
                           'name': 'United States of America'}],
 'release_date': '1956-02-02',
 'revenue': 0,
 'runtime': 102,
 'spoken_languages': [{'english_name': 'English',
                       'iso_639_1': 'en',
                       'name': 'English'}],
 'status': 'Released',
 'tagline': '',
 'title': 'The Benny Goodman Story',
 'video': False,
 'vote_average': 6.2,
 'vote_count': 11}
'''
```

