# 데이터베이스

- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 하나 이상의 자료의 모음
- 즉, 몇 개의 자료 파일을 **조직적으로 통합**하여 **중복을 없애고** **구조화**하여 **기억**시킨 자료의 집합체

## 데이터베이스의 장점

- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보 보장)
- 데이터 일관성
- 데이터 독립성 (물리적 / 논리적)
- 데이터 표준화
- 데이터 보안 유지

## RDB (Relational Database)

- 관계형 데이터베이스

  - 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형

  - 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스

    | 고유 번호 |  이름  | 주소 | 나이 |
    | :-------: | :----: | :--: | :--: |
    |     1     | 홍길동 | 제주 |  20  |
    |     2     | 김철수 | 서울 |  30  |
    |     3     | 박영희 | 독도 |  40  |

- 스키마 (schema)

  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것

    | column  | datatype |
    | :-----: | :------: |
    |   id    |   INT    |
    |  name   |   TEXT   |
    | address |   TEXT   |
    |   age   |   INT    |

- 테이블 (table)

  - 열 (column / field)과 행 (record / value)의 모델을 사용해 조직된 데이터 요소의 집합

    |  id  |  name  | address | age  |
    | :--: | :----: | :-----: | :--: |
    |  1   | 홍길동 |  제주   |  20  |
    |  2   | 김철수 |  서울   |  30  |
    |  3   | 박영희 |  독도   |  40  |

  - 열 : 각 열에 고유한 데이터 형식 지정

  - 행 : 실제 데이터가 저장되는 형태

  - 기본 키 (Primary Key) : 각 행의 고유 값, 반드시 설정해야 하며 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨

## RDBMS

- 관계형 데이터베이스 관리 시스템
  - 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템을 의미
  - ORACLE, MySQL, SQLite, ...

### SQLite

- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스

- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨

- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용 가능

- SQLite Data Type

  1. NULL
  2. INTEGER : 크기에 따라 0, 1, 2, 3, 4, 5, 6 또는 8 바이트에 저장된 부호 있는 정수
  3. REAL : 8 바이트 부동 소수점 숫자로 저장된 부동 소수점 값
  4. TEXT
  5. BLOB : 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

- SQLite Type Affinity : 특정 열에 저장하도록 권장하는 데이터 타입

  1. INTEGER
  2. TEXT
  3. BLOB
  4. REAL
  5. NUMERIC

  |    Example Typenames From The<br/>CREATE TABLE Statement     | Resulting Affinity |
  | :----------------------------------------------------------: | :----------------: |
  | INT<br/>INTEGER<br/>TINYINT<br/>SMALLINT<br/>MEDIUMINT<br/>BIGINT<br/>UNSIGNED BIG INT<br/>INT2<br/>INT8 |      INTEGER       |
  | CHARACTER(20)<br/>VARCHAR(255)<br/>VARYING CHARACTER(255)<br/>NCHAR(55)<br/>NATIVE CHARACTER(70)<br/>NVARCHAR(100)<br/>TEXT<br/>CLOB |        TEXT        |
  |               BLOB<br/>(no datatype specified)               |        BLOB        |
  |        REAL<br/>DOUBLE<br/>DOUBLE PRECISION<br/>FLOAT        |        REAL        |
  | NUMERIC<br/>DECIMAL(10,5)<br/>BOOLEAN<br/>DATE<br/>DATETIME  |      NUMERIC       |

## SQL (Structured Query Language)

- 관계형 데이터베이스 관리 시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

|                          분류                           |                             개념                             |                   예시                   |
| :-----------------------------------------------------: | :----------------------------------------------------------: | :--------------------------------------: |
|  DDL - 데이터 정의 언어<br/>(Data Definition Language)  | 관계형 데이터베이스 구조(테이블, 스키마)를<br/>정의하기 위한 명령어 |        CREATE<br/>DROP<br/>ALTER         |
| DML - 데이터 조작 언어<br/>(Data Manipulation Language) |  데이터를 저장, 조회, 수정, 삭제 등을<br/>하기 위한 명령어   | INSERT<br/>SELECT<br/>UPDATE<br/>DELETE  |
|   DCL - 데이터 제어 언어<br/>(Data Control Language)    |  데이터베이스 사용자의 권한 제어를 위해<br/>사용하는 명령어  | GRANT<br/>REVOKE<br/>COMMIT<br/>ROLLBACK |

- SQL Keywords - Data Manipulation Language
  - `INSERT` : 새로운 데이터 삽입(추가)
  - `SELECT` : 저장되어 있는 데이터 조회
  - `UPDATE`: 저장되어 있는 데이터 갱신
  - `DELETE` : 저장되어 있는 데이터 삭제

## DB 실습

### CREATE, DROP

- 데이터베이스 생성하기

  ```bash
  $ sqlite3 tutorial.sqlite3
  sqlite> .database
  ```

- csv 파일을 table로 만들기

  ```bash
  sqlite> .mode csv
  sqlite> .import hellodb.csv examples
  sqlite> .tables
  examples
  sqlite> SELECT * FROM examples;
  1,"길동","홍",600,"충청도",010-0000-0000
  ```

- `CREATE TABLE` 

  - 데이터베이스에서 테이블 생성

  ```sql
  CREATE TABLE classmates (
      id INTEGER PRIMARY KEY,
      name TEXT
  );
  ```

  ```bash
  sqlite> CREATE TABLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT
     ...> );
  sqlite> .tables
  classmates examples
  ```

- 특정 테이블의 schema  조회

  ```bash
  sqlite> .schema classmates
  CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
  );
  ```

- `DROP TABLE`

  - 데이터베이스에서 테이블 제거

  ```bash
  sqlite> DROP TABLE classmates;
  sqlite> .tables
  examples
  ```

- 필드 제약 조건

  - NOT NULL : NULL 값 입력 금지
  - UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
  - PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키. 다른 테이블의 Key
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값

### INSERT

- 테이블에 단일 행 삽입

  ```sql
  INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
  ```

- 테이블에 정의된 모든 열에 맞춰 순서대로 입력

  ```sql
  INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
  ```

- `rowid` : SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PRIMARY KEY 열

  ```bash
  sqlite> SELECT rowid, * FROM classmates;
  rowid       name        age         address
  ----------  ----------  ----------  ----------
  1           홍길동       23
  2           홍길동       30          서울
  ```

  - 만약 스키마에 id 기본키를 직접 작성할 경우, 입력할 column들을 명시하지 않으면 자동으로 입력되지 않음

    ```sql
    INSERT INTO classmates VALUES (1, '홍길동', 30, '서울'); 
    # id를 포함한 모든 value를 작성
    
    INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울'); 
    # 각 value에 맞는 column들을 명시적으로 작성
    ```

- 여러 값 한번에 넣기

  ```sql
  INSERT INTO classmates VALUES
  ('홍길동', 30, '서울'), 
  ('김철수', 30, '제주'),
  ('이호영', 26, '인천'),
  ('박민희', 29, '대구'),
  ('최혜영', 28, '전주');
  ```

### SELECT

```sql
SELECT col1, col2, ... FROM table_name;
SELECT * FROM table_name;
```

- 테이블에서 데이터를 조회

- 가장 기본이 되는 문이며 다양한 절과 함께 사용

  - `ORDER BY`, `DISTINCT`, `WHERE`, `LIMIT`, `GROUP BY` …

  - `LIMIT`

    - 쿼리에서 반환되는 행 수를 제한
    - 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용하기도 함

  - `OFFSET`

    - 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

    - 0부터 시작함

      ```sql
      SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5;
      # 6번째 행 부터 10개 행을 조회 (6번째 행부터 10개를 출력)
      ```

  - `WHERE`

    - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

  - `SELECT DISTINCT`

    - 조회 결과에서 중복 행을 제거
    - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

  - `ORDER BY`

    - 쿼리에서 반환되는 행을 특정 열을 기준으로 오름차순 혹은 내림차순 정렬

  - `GROUP BY`

    - 특정 열에 대해 같은 값을 가진 행끼리 묶어서 그룹화
    - 그룹화한 결과에 조건 처리를 하기 위해선 `HAVING` 절을 사용해야 함

