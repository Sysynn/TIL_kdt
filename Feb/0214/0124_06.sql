-- 문제 1
CREATE TABLE users (
userId INT NOT NULL AUTO_INCREMENT,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
birthday DATETIME NOT NULL,
city VARCHAR(100) NULL,
country VARCHAR(100) NULL,
email VARCHAR(100) NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (userId)
);

SHOW COLUMNS FROM users;

-- 문제 2
INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
 ('Beemo', 'Jeong', '1000-01-01', NULL, NULL, 'beemo@hphk.kr'),
 ('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', NULL),
 ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', NULL),
 ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', NULL);
 
 SELECT * FROM users;
 
 INSERT INTO users (first_name, last_name, birthday, city, country, email)
VALUES
 ('Liel', 'Abada', '2001-10-3', NULL, 'Israel', 'labada@gmail.com'),
 ('Heungmin', 'Son', '1992-07-08', 'Chuncheon', 'Korea', NULL),
 ('Mikel', 'Arteta', '1982-03-26', NULL, 'Spain', NULL),
 ('Samsik', 'Kim', '1872-03-26', NULL, 'Korea', NULL),
 ('Erling', 'Haaland', '2000-07-21', NULL, 'Norway', NULL);

-- 문제 4
UPDATE users
SET 
 first_name = 'Sangyoon',
 last_name = 'Shin',
 birthday = '1011-12-25'
WHERE
 userId = 2;
 
-- 문제 5
UPDATE users
SET country = 'Korea'
WHERE country IS NULL;

-- 문제 6
DELETE FROM 
 users
WHERE 
 first_name = 'Beemo';
 
-- 문제 7
DELETE FROM 
 users
WHERE 
 first_name = 'Kwangsoo' AND last_name = 'Lee';
 
 -- 문제 8
DELETE FROM
 users
ORDER BY
 created_at DESC
 LIMIT 1;