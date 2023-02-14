# CREATE TABLE
- CREATE와 DROP 문을 통해 테이블을 생성 및 삭제할 수 있다
- MySQL의 데이터 타입 및 제약 조건을 사용하여 요구사항에 맞는 스키마를 작성할 수 있다

## Create a table
1. CREATE TABLE 
```
CREATE TABLE table_name(
    column_1 data_type,
    column_2 data_type,
    ,,,,
    constraints
);
```
- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건(constratints) 작성 

```
CREATE TABLE examples (
    examID INT AUTO_INCREMENT,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    PRIMARY KEY (examID)
);
```
```
-- Table 구조 확인
SHOW COLUMNS FROM examples;
```
1. 이름을 정하고
2. 이 테이블이 어떤 타입인지 정하고
3. 어떤 제약조건을 가지고 있는지 정한다.
4. 공백으로 구분하고 쉼표(,)는 조건이 끝났을때 사용
5. NOT NULL은 빈 칸에 NULL 값을 넣지 않겠다는 의미
6. 다른 테이블과 어떻게 식별할지를 위해 Primary Key 가 필요함

```
SHOW COLUMNS FROM examples;
```
- 컬럼들을 확인한다


 Numer ic       숫자형  INT, FLOAT, ...

 String         문자형  VARCHAR, TEXT, ...

 Date and Time  날짜형  DATE, DATETIME, ...


## Constraint
데이터의 무결성을 지키기 위해 데이터를 입력 받을 때 실행하는 규칙
-> 데이터의 정확성과 일관성을 보증 (아무데이터나 받지않는다)

### 대표적인 MySQL Constraints
1. PRIMARY KEY
- 해당 필드를 기본 키로 지정
2. NOT NULL
- 해당 필드에 NULL 값을 저장하지 못하도록 지정

## AUTO_INCREMENT
- 테이블의 기본 키에 대한 번호 자동 생성
### AUTO_INCREMENT 특징
- 기본 키 필드에 사용
 - 고유한 숫자를 부여
- 시작 값은 1이며 데이터 입력 시 값을 생략하면 자동으로 1씩 증가
- 이미 사용한 값을 재사용하지 않음
- 기본적으로 NOT NULL 제약 조건을 포함

예를들어 게시판에 글을 쓸 때 게시글 번호를 작성자가 직접 작성하지 않는 것처럼...


# DELETE TABLE

## DROP TABLE 
(DELETE가 아님!)

```
DROP TABLE table_name;
```

# ALTER TABLE
- 테이블 필드 조작 
 -> 이거 하나로 테이블 필드를 생성, 수정, 삭제할 수 있다

 ```
 ALTER TABLE ADD          필드 추가
 ALTER TABLE MODIFY       필드 속성 변경
 ALTER TABLE CANGE COLUMN 필드 이름 변경
 ALTER TABLE DROP COLUMN  필드 삭제
 ```

 ## ALTER TABLE ADD

```
ALTER TABLE
    table_name
ADD
    new_column_name column_definition;
```
- ADD 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성

## ALTER TABLE MODIFY
- MODIFY 키워드 이후 변경하고자 하는 필드 이름 그리고 데이터 타입 및 제약조건 작성
- ADD 와 구조는 같다
- 바꿀 부분만 수정하는 것이 아니라 아예 새로 선언하는 느낌

## ALTER TABLE CHANGE COLUMN
```
ALTER TABLE
    examples
CHANGE COLUMN
    country state VARCHAR(100) NOT NULL;
```
- CHANGE COLUMN 바꿀 이름 새 이름
- CHANGE COLUMN은 MODIFY의 기능도 같이 수행함
(분명히 이름을 바꾸는건데 조건까지 새로 써야함...)

## ALTER TABLE DROP COLUMN 
```
ALTER TABLE
    table_name
DROP COLUMN
    column_name;
```
- DROP COLUMN 키워드 이후 삭제하고자 하는 필드 이름 작성

# SQL - Modifying Data

## INSERT statement
- 테이블 레코드 삽입 (CREATE 가 아님 헷갈림 주의)
```
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...)
```
- INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성

* CURDATE() : 현재 날짜 값 반환, MySQL 이 제공하는 Date Function 중 하나

## UPDATE
```
UPDATE table_name
SET column_name = expression,
[WHERE
    condition];
```
- SET 절 다음에 수정할 필드와 새 값 지정
- WHERE 절에서 수정할 레코드를 지정하는 조건 작성 (없으면 모든 레코드 수정)

## DELETE statement

```
DELETE FROM table_name
[WHERE
    condition];]
```
- WHERE 절이 없으면 모든 곳을 다 삭제