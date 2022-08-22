CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT,
    role_id INT
);

INSERT INTO users VALUES 
    (1, '관리자', 1),
    (2, '김철수', 2),
    (3, '이영희', 2);

CREATE TABLE role (
    id INT PRIMARY KEY, 
    title TEXT
);

INSERT INTO role VALUES 
    (1, 'admin'),
    (2, 'staff'),
    (3, 'student');

CREATE TABLE articles (
    id INT PRIMARY KEY, 
    title TEXT,
    content TEXT,
    user_id INT
);

INSERT INTO articles VALUES 
    (1, '1번글', '111', 1),
    (2, '2번글', '222', 2),
    (3, '3번글', '333', 1),
    (4, '4번글', '444', NULL);

-- 확인
.mode column
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;