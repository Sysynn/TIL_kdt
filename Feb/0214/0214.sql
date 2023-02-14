CREATE TABLE examples(
	examID INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examID)
);

SHOW COLUMNS FROM examples;

DROP TABLE examples;
ALTER TABLE
	examples
ADD
	country VARCHAR(100) NOT NULL;

ALTER TABLE examples
ADD age INT NOT NULL,
ADD address VARCHAR(100) NOT NULL;

ALTER TABLE examples
MODIFY address VARCHAR(50) NOT NULL;

ALTER TABLE examples 
MODIFY lastName VARCHAR(10) NOT NULL, 
MODIFY firstName VARCHAR(10) NOT NULL;

ALTER TABLE examples
CHANGE COLUMN country state VARCHAR(100) NOT NULL;

ALTER TABLE examples
DROP COLUMN address;
    
ALTER TABLE examples
DROP COLUMN state,
DROP COLUMN age;

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL,
    PRIMARY KEY (id)
);

SHOW COLUMNS FROM articles;

SELECT * FROM articles;

INSERT INTO articles (title, content, createdAt) VALUES ("hello", "world", "2000-01-01");

INSERT INTO articles (title, content, createdAt) VALUES ("title1", "content1", "2000-01-01"), ("title2", "content2", "1900-01-01"), ("title3", "content3", "1800-01-01");

INSERT INTO articles (title, content, createdAT) VALUES ("mytitle", "mycontent", CURDATE());

UPDATE articles SET title = "newTitle" WHERE id = 1;

INSERT INTO articles(title, content, createdAt) VALUES ('mytitle', 'mycontent', CURDATE());

UPDATE articles SET content = REPLACE(content, 'content', 'TEST');
DELETE FROM articles WHERE id = 1;

DELETE FROM articles ORDER BY createdAt DESC LIMIT 2;