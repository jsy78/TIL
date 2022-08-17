-- classmates
-- name : TEXT
-- age : INT
-- address : TEXT 

CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);

-- CREATE TABLE students(
-- id INTEGER PRIMARY KEY,
-- name TEXT NOT NULL,
-- age INTEGER DEFAULT 1 CHECK (0 < age)
-- );

-- CREATE
-- INSERT INTO classmates VALUES ('홍길동', 23);
-- Parse error: table classmates has 3 columns but 2 values were supplied
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 40, '서울');

SELECT rowid, * FROM classmates;
-- rowid는 SQLite에서 자동으로 제공하고 있는 PK. 값이 1씩 증가하는 모습을 보임.
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   23
-- 2      홍길동   23   서울
-- 3      김철수   40   서울

DROP TABLE classmates;