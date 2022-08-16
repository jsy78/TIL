# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```

```
COUNT(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
```

```
COUNT(*)
--------
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 AND is_drinking = 1;
```

```
COUNT(*)
--------
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 AND va_right >= 2.0;
```

```
COUNT(*)
--------
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```

```
sido
----
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 모든 신장을 중복 없이 내림차순 출력
```sql
SELECT DISTINCT height FROM healthcare ORDER BY height DESC;
```

```
height
------
195
190
185
180
175
170
165
160
155
150
145
140
135
130
```
> 각 신장에 대응되는 사람들이 10000명 이상인 신장과 그 신장에 대응되는 사람들의 수를 사람들의 수 내림차순으로 출력
```sql
SELECT height, COUNT(*) FROM healthcare GROUP BY height HAVING COUNT(*) >= 10000 ORDER BY COUNT(*) DESC;
```

```
height  COUNT(*)
------  --------
160     184993
155     181306
165     179352
170     152585
150     128555
175     79531
145     50044
180     24312
140     12373
```
