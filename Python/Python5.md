# 모듈

- 다양한 기능을 하나의 파일로 (모듈)

- 다양한 파일을 하나의 폴더로 (패키지)

- 다양한 패키지를 하나의 묶음으로 (라이브러리)

- 이 모든 것들을 관리하는 관리자 : pip

## 모듈과 패키지

- 모듈 : 특정 기능을 하는 코드를 파이썬 파일 단위로 작성한 것
- 패키지 : 특정 기능과 관련된 여러 모듈의 집합. 패키지 안에는 또 다른 서브 패키지를 포함

## 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수
- 예시
  - [datetime — 기본 날짜와 시간 형 — Python 3.10.5 문서](https://docs.python.org/ko/3/library/datetime.html)
  - [math — 수학 함수 — Python 3.10.5 문서](https://docs.python.org/ko/3/library/math.html)
  - [random — 의사 난수 생성 — Python 3.10.5 문서](https://docs.python.org/ko/3/library/random.html)



# 파일 입출력

- `open`(*file*, *mode='r'*, *buffering=- 1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)

  ```python
f = open('workfile', 'w', encoding="utf-8")
  ```
  - *file* 을 열고 해당 파일 객체를 돌려주고 파일을 열 수 없으면, OSError가 발생
  
  
  | 문자  | 의미                                                         |
| :---- | :----------------------------------------------------------- |
  | `'r'` | 읽기 용으로 열기 (기본값)                                    |
| `'w'` | 쓰기 용으로 열기, 파일을 먼저 잘라냄                         |
| `'x'` | 독점적인 파일 만들기 용으로 열기, 이미 존재하는 경우에는 실패함 |
| `'a'` | 만약 파일이 존재하는 경우 추가 쓰기 용으로 열기              |
| `'b'` | 바이너리 모드                                                |
| `'t'` | 텍스트 모드 (기본값)                                         |
| `'+'` | 갱신(읽기 및 쓰기)용으로 열기                                |

- 공식적으로 with 구문을 활용하는 것을 권장함

  ```python
  with open('workfile', encoding="utf-8") as f:
      read_data = f.read()
  ```

  - with 구문을 쓰지 않으면 파일을 열고 작업이 끝나면 일일이 close를 호출해 닫아줘야 함
- with 구문을 활용하면 블록이 끝나면 자동으로 안전하게 파일이 닫힘
  | 메소드          | 설명                                                         |
  | --------------- | ------------------------------------------------------------ |
  | f.read(size)    | 일정량의 데이터를 읽고 문자열이나 바이너리 타입으로 돌려줌, size가 생략되면 파일 전체를 읽어서 돌려줌 |
  | f.readline()    | 파일을 한 줄씩 읽어서 돌려줌                                 |
  | f.readlines()   | 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 돌려줌 |
  | f.write(string) | string의 내용을 파일에 쓰고 출력된 문자들의 개수를 돌려줌    |

- 파일을 한 줄씩 읽는 반복문 예시

  ```python
  for line in f:
      print(line, end='')
  ```


## JSON 활용

```json
{
    "adult": false,
    "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
    "genre_ids": [
        18,
        80
    ],
    "id": 278,
    "original_language": "en",
    "original_title": "The Shawshank Redemption",
    "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
    "popularity": 67.931,
    "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
    "release_date": "1995-01-28",
    "title": "쇼생크 탈출",
    "video": false,
    "vote_average": 8.7,
    "vote_count": 18040
}
```

```json
[
  {
    "id": 28,
    "name": "Action"
  },
  {
    "id": 12,
    "name": "Adventure"
  },
  {
    "id": 80,
    "name": "Crime"
  },
  {
    "id": 99,
    "name": "Documentary"
  },
  {
    "id": 10402,
    "name": "Music"
  },
  {
    "id": 37,
    "name": "Western"
  }
]
```

- 내용의 구조가 파이썬의 딕셔너리, 리스트와 유사한 것들 알 수 있음

- `json`이라는 표준 모듈은 파이썬 데이터 계층을 받아서 문자열 표현으로 바꿔줄 수 있음 (`import json` 필요)

- json 파일을 열고, json.load()를 쓰면 json 파일의 내용을 파이썬 객체 형식으로 변환 가능

  ```python
  movie_json = open('data/movie.json', 'r', encoding='utf-8')
  movie = json.load(movie_json)
  ```

- 첫 번째 파일은 딕셔너리로, 두 번째 파일은 리스트로 변환됨
