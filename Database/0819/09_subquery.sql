-- 가장 나이가 작은 사람의 수
-- 1
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;
-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 확인해보기
SELECT MIN(age) 
FROM users;
-- MIN(age)
-- --------
-- 15

SELECT COUNT(*)
FROM users 
WHERE age = 15;
-- COUNT(*)
-- --------
-- 39

SELECT COUNT(*)
FROM users 
WHERE age = (SELECT MIN(age) FROM users);
-- COUNT(*)
-- --------
-- 39

-- 평균 계좌 잔고가 높은 사람은 수?

SELECT AVG(balance) FROM users;

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
-- COUNT(*)
-- --------
-- 222

-- 유은정과 같은 지역에 사는 사람의 수?
SELECT 
    country
FROM users
WHERE last_name = '유' AND first_name = '은정';

SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '유' AND first_name = '은정');

-- 당연히
SELECT COUNT(*), AVG(balance), AVG(age)
FROM users;

-- 예를 들면
-- table이 게시글 테이블, 댓글 테이블
SELECT 
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉;
-- 총인원   평균연봉
-- ----  ---------
-- 1000  151456.89

-- 이은정
SELECT 
    country
FROM users
WHERE last_name = '이' AND first_name = '은정';
-- country
-- -------
-- 전라북도
-- 경상북도

SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 115

SELECT country, COUNT(*)
FROM users
GROUP BY country;
-- country  COUNT(*)
-- -------  --------
-- 강원도      101
-- 경기도      114
-- 경상남도     106
-- 경상북도     103
-- 전라남도     123
-- 전라북도     115
-- 제주특별자치도  118
-- 충청남도     105
-- 충청북도     115

SELECT 
    COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 218

-- 특정 성씨별로 가장 적은 나이 사람 모두
SELECT 
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;

SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT 
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;