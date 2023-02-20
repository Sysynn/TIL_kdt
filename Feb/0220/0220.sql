DROP TABLE users;
-- 자동 COMMIT 비활성화
SET autocommit = 0;

-- user 테이블 생성
CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);

START TRANSACTION;
INSERT INTO users (name)
VALUES ('harry'), ('test');

SELECT * FROM users;


-- ROLLBACK;

COMMIT;

DROP TABLE articles;
-- 사전 준비 / articles 테이블 작성 및 예시 데이터 입력
CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY(id)
);
SELECT * FROM articles;
INSERT INTO articles (title, createdAt, updatedAt)
VALUES ('title1', CURRENT_TIME(), CURRENT_TIME());

DELIMITER //
CREATE TRIGGER myTrigger
	-- 언제?
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
	SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;

SHOW TRIGGERS;

UPDATE articles
SET title = 'new title'
WHERE id = 1;

-- Practice #2 사전준비
CREATE TABLE articleLogs (
	id INT AUTO_INCREMENT,
    description VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER myLog
	AFTER INSERT
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO articleLogs (description, createdAt)
    VALUES (CONCAT(NEW.id, '글이 작성되었습니다.'), CURRENT_TIME());
END//
DELIMITER ;
SHOW TRIGGERS;
INSERT INTO articles (title, createdAt, updatedAt)
VALUES('title', CURRENT_TIME(), CURRENT_TIME());

DROP TRIGGER myLog;

SELECT * FROM articles;
SELECT * FROM articleLogs;

-- Tiggers Practice #3 사전준비
CREATE TABLE backupArticles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    PRIMARY KEY (id)
);

DELIMITER //
CREATE TRIGGER backupLog
	AFTER DELETE
    ON articles FOR EACH ROW
BEGIN
	INSERT INTO backupArticles (title, createdAt, updatedAt)
    VALUES (OLD.title, OLD.createdAt, OLD.updatedAt);
END//
DELIMITER ;

DELETE FROM articles
WHERE id = 1;
SELECT * FROM backupArticles;