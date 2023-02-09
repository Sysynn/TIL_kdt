# SQL
- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- 즉, CRUD!! 로 역할이 제한되어 있다고 볼 수 있음
- Structure Query Language

## SQL Syntax
- 예를 들어 Google에 작성하는 아래와 같은 질문은
```
    how old is earth
```
SQL로 보면 
```
    SELECT age FROM solar_system WHERE name = 'earth'
```
- SQL 키워드는 대소문자를 구분하지 않음
    - 하지만 대문자로 작성하는 것을 권장 (명시적 구분))
- 각 SQL Statements 의 끝에는 세미콜론(;)이 필요
    - 세미콜론은 각 SQL Statements을 구분하는 방법

# SQL Statement
SQL 언어를 실행하기 위한 가장 기본적인 코드 블록 (SQL문)

## 예시
```
SELECT column_name FROM table_name;
```
- 해당 예시 코드는 SELECT Statement라 부름
- 이 Statement는 SELECT, FROM 2 개의 Keyword(절)로 구성됨

## SQL Statements 유형
- 데이터베이스에서 수행목적에 따라 대체로 4가지 범주로 나뉨
    - DDL - 데이터 정의
    - DQL - 데이터 검색
    - DML - 데이터 조작
    - DCL - 데이터 제어
## 정리
- SQL은 데이터베이스와 상호작용하고 데이터베이스에서 데이터를 반환하기 위한 언어
- 단순히 SQL 문법을 암기하고 상황에 따라 실행만 하는 것이 아닌
SQL을 통해 관계형 데이터베이스를 잘 이해하고 다루는 방법을 연습 

## SQL - Single Table Queries
```
1. Querying data (기본)
2. Sorting data (정렬)
3. Filtering data
4. Grouping data
```
### 1. Querying data
> SELECT statement - 테이블에서 데이터를 조회
```mySQL
SELECT
   select_list
FROM
   table_name;
```
연산도 가능하다 
```
SELECT
    productCode,
    quantityOrdered * priceEach AS '주문총액'
FROM
    orderdetails;
```

- SELECT 키워드 다음에 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 키워드 다음에 데이터를 선택하려는 테이블의 이름을 지정

### 2. Sorting data
> ORDER BY clause - 조회 결과의 레코드를 정렬
```
SELECT
    select_list
FROM
ORDER BY
    column1 [ASC:DESC],
    column2 [ASC:DESC],
    ...;
```
ASC 오름차순
DESC 내림차순

오름차순 조회
```
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName;
```
- 정렬의 기준을 firstName으로 해서 오름차순으로 정렬

```
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName DESC;
```
- 내림차순으로 정렬

