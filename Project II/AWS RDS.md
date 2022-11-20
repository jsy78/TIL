# AWS RDS

```
❓ 이 가이드는
RDS - PostgreSQL / Django 설정 
2개로 구분됩니다.

AWS는 잘못된 사용을 할 경우 많은 과금이 발생할 수도 있습니다.
두 개 이상의 RDS 인스턴스를 생성하면 과금이 발생할 수 있습니다.
가이드를 잘 보고 따라해주세요.
```

```
🇰🇷 지역 설정 - 서울
경고 : 다른 지역에서 생성한 RDS는 모두 삭제해야 합니다.
```

![Untitled](./AWS%20RDS/Untitled.png)

# RDS - PostgreSQL

```
❓ AWS RDS?
S3가 파일을 저장하는 클라우드 파일 스토리지 서비스라면
RDS는 데이터를 저장하는 클라우드 데이터베이스 서비스입니다.
경고 : 2개 이상(타 지역 포함)의 데이터베이스를 생성할 경우 과금이 발생합니다.
```

### 데이터베이스 생성

![Untitled](./AWS%20RDS/Untitled%201.png)

```
⚠️ ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️ 주의 ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
`엔진 옵션 - PostgreSQL`
`템플릿 - 프리 티어` (다른 템플릿 선택으로 인한 과금 발생에 대한 책임을 지지 않음.)
```

![Untitled](./AWS%20RDS/Untitled%202.png)

```
📌 DB 인스턴스 식별자 - 자유 입력
마스터 암호 / 암호 확인 - 자유 입력 (패스워드 기록)
```

![Untitled](./AWS%20RDS/Untitled%203.png)

```
📌 스토리지
스토리지 자동 조정 활성화 - 해제
```

![Untitled](./AWS%20RDS/Untitled%204.png)

```
📌 연결
`퍼블릭 액세스 - 예 선택`

VPC 보안 그룹 새로 생성
`새 VPC 보안 그룹 입력 - 자유 입력`
```

![Untitled](./AWS%20RDS/Untitled%205.png)

```
📌 모니터링 
`성능 인사이트 켜기 - 해제`
```

![Untitled](./AWS%20RDS/Untitled%206.png)

```
📌 추가 구성 - 데이터베이스 옵션
`초기 데이터베이스 이름 - 데이터베이스 이름 자유 입력`

추가 구성 - 백업
`자동 백업을 활성화합니다. - 해제`
```

![Untitled](./AWS%20RDS/Untitled%207.png)

```
📌 데이터베이스 생성
생성까지 약 10분의 시간이 필요합니다.
```

![Untitled](./AWS%20RDS/Untitled%208.png)

### 보안 그룹 설정

```
📌 생성한 데이터베이스 클릭
생성한 VPC 보안 그룹 클릭
```

![Untitled](./AWS%20RDS/Untitled%209.png)

```
📌 인바운드 규칙 편집
```

![Untitled](./AWS%20RDS/Untitled%2010.png)

```
📌 규칙 추가
1️⃣ PostgreSQL - Anywhere-IPv4
2️⃣ PostgreSQL - Anywhere-IPv6
3️⃣ 규칙 저장
```

![Untitled](./AWS%20RDS/Untitled%2011.png)

# 장고 설정

### RDS 연결 테스트

```
📌 개발 환경(로컬)에서 RDS 연결 테스트
```

```bash
# postgresql 관리 패키지 설치
pip install psycopg2-binary
pip freeze > requirements.txt
```

```dart
# settings.py 작성

"""
기존 DATABASES 주석 처리
"""
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "[데이터베이스 이름]", # 코드 블럭 아래 이미지 참고하여 입력
        "USER": "postgres",
        "PASSWORD": "[패스워드]", # 데이터베이스 생성 시 작성한 패스워드
        "HOST": "[엔드포인트]", # 코드 블럭 아래 이미지 참고하여 입력
        "PORT": "5432",
    }
}
```

```
📌 데이터베이스 이름
```

![Untitled](./AWS%20RDS/Untitled%2012.png)

```
📌 엔드포인트
```

![Untitled](./AWS%20RDS/Untitled%2013.png)

```
📌 마이그레이트
```

```python
python manage.py makemigrations
python manage.py migrate
```

### 환경 분리

```
📌 개발 환경(sqlite) / 배포 환경(postgresql) 설정 분리
```

```bash
# dotenv 패키지 설치
pip install python-dotenv
```

```python
# settings.py

"""
최상단에 아래 세 줄 추가
"""
from dotenv import load_dotenv
import os
load_dotenv()

# ------------------------------
"""
기존 DATABASES 설정 삭제
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "[데이터베이스 이름]", # 코드 블럭 아래 이미지 참고하여 입력
        "USER": "postgres",
        "PASSWORD": "[패스워드]", # 데이터베이스 생성 시 작성한 패스워드
        "HOST": "[엔드포인트]", # 코드 블럭 아래 이미지 참고하여 입력
        "PORT": "5432",
    }
}
"""

DEBUG = os.getenv("DEBUG") == "True"

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
		"""
		# 기타 개발 환경 설정 작성
		# ...
		"""

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"), # .env 파일에 value 작성
            "USER": "postgres",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"), # .env 파일에 value 작성
            "HOST": os.getenv("DATABASE_HOST"), # .env 파일에 value 작성
            "PORT": "5432",
        }
    }
		"""
		# 기타 배포 환경 설정 작성
		# ...
		"""

```

```
📌 manage.py 파일과 동일한 위치에 .env 파일 생성 및 내용 작성
```

```
# .env
# 각 key에 해당하는 value 작성
DATABASE_HOST = [엔드포인트]
DATABASE_PASSWORD = [패스워드]
DATABASE_NAME = [데이터베이스 이름]
DEBUG = True
```

# VScode PostgreSQL 데이터베이스 연결

```
📌 확장프로그램 - PostgreSQL 설치
```

![Untitled](./AWS%20RDS/Untitled%2014.png)

```
📌 데이터베이스 연결
```

![Untitled](./AWS%20RDS/Untitled%2015.png)

![Untitled](./AWS%20RDS/Untitled%2016.png)

![Untitled](./AWS%20RDS/Untitled%2017.png)

![Untitled](./AWS%20RDS/Untitled%2018.png)

![Untitled](./AWS%20RDS/Untitled%2019.png)

![Untitled](./AWS%20RDS/Untitled%2020.png)

![Untitled](./AWS%20RDS/Untitled%2021.png)

![Untitled](./AWS%20RDS/Untitled%2022.png)

```
📌 데이터베이스 연결 확인
각 테이블을 오른쪽 클릭하면 데이터 조회(SELECT) 가능
```

![Untitled](./AWS%20RDS/Untitled%2023.png)