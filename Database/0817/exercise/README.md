# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

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

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;
```

```
MAX(height)  MIN(height)  MAX(weight)  MIN(weight)
-----------  -----------  -----------  -----------
195          130          135          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE height BETWEEN 160 AND 170;
```
```sql
SELECT COUNT(*) FROM healthcare WHERE height >= 160 AND height <= 170;
```

```
COUNT(*)
--------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
SELECT waist FROM healthcare WHERE is_drinking = 1 AND waist LIKE '_%' ORDER BY waist DESC LIMIT 5;
```
```sql
SELECT waist FROM healthcare WHERE is_drinking = 1 AND waist != '' ORDER BY waist DESC LIMIT 5;
```
```sql
SELECT waist FROM healthcare WHERE is_drinking = 1 AND NOT waist = '' ORDER BY waist DESC LIMIT 5;
```

```
waist
-----
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 1.5 AND va_right >= 1.5 AND is_drinking = 1;
```

```
COUNT(*)
--------
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE blood_pressure < 120;
```

```
COUNT(*)
--------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
AVG(waist)
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
```

```
AVG(height)       AVG(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
```

```
id      height  weight
------  ------  ------
836005  195     110
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE weight*10000/(height*height) >= 30;
```

```
COUNT(*)
--------
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, weight*10000/(height*height) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY BMI DESC LIMIT 5;
```

```
id      BMI
------  ---
231431  50
934714  49
722707  48
947281  47
948801  47
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

> BMI 지수가 높은 순서대로 5명의 허리둘레와 BMI 출력

```sql
SELECT weight*10000/(height*height) AS BMI, waist FROM healthcare ORDER BY BMI DESC LIMIT 5;
```

```
BMI  waist
---  -----
57   136.0
54   130.0
52   123.0
52   128.0
52   121.0
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

> 각 시도별 평균 신장, 평균 체중, 평균 BMI 출력

```sql
SELECT sido, AVG(height), AVG(weight), AVG(weight/(height*height*0.0001)) AS BMI FROM healthcare GROUP BY sido;
```

```
sido  AVG(height)       AVG(weight)       BMI
----  ----------------  ----------------  ----------------
11    160.861241284718  62.6686358140178  24.2185094038135
26    160.988409996378  62.7108294096342  24.1965430303207
27    160.874661764402  62.289984095181   24.0681620183805
28    161.048847373382  63.6887479646928  24.5554258069909
29    161.248422823496  62.9841931865975  24.2237078228847
30    161.173769837309  62.8603985760389  24.1984975522225
31    162.600092304142  64.2904119072343  24.3166997677007
36    162.262383900929  63.7538699690402  24.2142402972667
41    161.375839333142  63.6257776843501  24.4318343676362
42    159.935202822971  62.9889454454611  24.62499815543
43    160.150842424064  62.5821106177776  24.400108129882
44    160.689023531069  63.2300032877742  24.4878570340893
45    159.787211684968  62.2922030158146  24.3977430836411
46    160.309928761074  63.006755868668   24.5169407059672
47    160.399996326096  62.4058562033873  24.2558578080029
48    161.333941339559  62.9085801838611  24.1689841135269
49    160.540495032834  63.9695234888028  24.820122466179
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

> 각 시도별 평균 허리 둘레가 82 이상인 곳의 시도와 평균 허리 둘레를 높은 순으로 상위 5군데만 출력

```sql
 SELECT sido, AVG(waist) FROM healthcare GROUP BY sido HAVING AVG(waist) >= 82 ORDER BY AVG(waist) DESC LIMIT 5;
```

```
sido  AVG(waist)
----  ----------------
49    84.2457905371274
46    82.9753318787633
44    82.9497675073983
31    82.6866543594474
28    82.6097951838207
```