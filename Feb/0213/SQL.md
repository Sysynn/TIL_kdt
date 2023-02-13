# Filtering data
## DISTINCT clause
 - 조회 결과에서 중복된 항목을 제거
 ```
 SELECT DISTICT
    select_list
FROM
    table_name;
```
- SELECT 바로 뒤에 작성
- SELECT DISTINCT 다음에 고유한 값을 선택하려는 하나 이상의 "필드"를 지정

```
SELECT DISTINCT lastName FROM employees ORDER BY lastName ASC;
```
- 결과에서 중복을 제거한다


## WHERE syntax
- Python에서 "if" 역할을 하면서 특정 조건을 검색

```
SELECT
    select_list
FROM
    table_name
WHERE
    search_condition;
```
- FROM 뒤에 위치
- search_condition운 비교연산자 및 논리연산자(AND, OR, NOT 등)를 사용하는 구문이 사용됨

```
SELECT lastName, firstName, officeCode, jobTitle FROM employees WHERE officeCode >= 3 AND jobTitle = "Sales Rep";
```
- 위 코드처럼 연산자도 사용 가능

```
SELECT lastName, firstName, officeCode FROM employees WHERE officeCode BETWEEN 1 AND 4;
```
- BETWEEN 은 숫자 사이를 조회 (입력 숫자를 포함!)
- ex) BETWEEN 1 AND 4; 라면 1 이상 4 이하.

```
SELECT lastName, firstName, officeCode FROM employees WHERE officeCode BETWEEN 1 AND 4 ORDER BY officeCode;
```
- ORDER BY 가 같이 쓰일 경우 WHERE 보다 뒤에 위치

```
SELECT lastName, firstName, officeCode FROM employees WHERE officeCode IN (1, 3, 4);
```
IN 을 써서 해당 항목을 포함하는 조건 검색
```
SELECT lastName, firstName FROM employees WHERE lastName LIKE "%son";
```
- LIKE 를 통해 패턴에 일치하는 값인지 확인

```
SELECT lastName, firstName FROM employees WHERE firstName LIKE "___y";
```
- %, ___ 등은 와일드카드라고 부름. ___는 자릿수까지 비교

## Operators
1. Comparison Operators 비교 연산자
- =, >=, <=, !=, IS, LIKE, IN, BETWEEN...AND
2. Logical Operators 논리 연산자
- AND(&&), OR(::), NOT(!)
3. IN operators
- 값이 특정 목록 안에 있는지 확인
4. LIKE operator 
- 값이 특정 패턴에 일치하는지 확인 (Wildecards의 도움을 받음)
- '%' : 0개 이상의 문자열과 일치하는지 확인 (0도 포함)
  '_' : 단일 문자와 일치하는지 확인
5. LIMIT clause
- 조회하는 레코드 수 제한
- FROM 뒤에 위치
- row_count는 조회할 최대 레코드 수를 지정
- LIMIT 10; 이라고 하면, 10개까지만 보여줌
- LIMIT 3, 5; 라고 하면, "3개를 건너 뛰고" 5개 조회 (3부터 5가 아님)
- offset은 시작점을 변경
6. GOUP BY clause
- 레코드를 그룹화하여 요약본 생성 with 집계 함수
- 집계함수 (Aggregation Functions)
 - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
 - SUM, AVG, MAX, MIN, COUNT
```
SELECT jobTitle, COUNT(*) FROM employees GROUP BY jobTitle;
```
- GROUP BY는 FROM 및 WHERE 절 뒤에 배치

7. HAVING
```
SELECT country, AVG(creditLimit) AS averageOfCreditLimit FROM customers GROUP BY country HAVING averageOfCreditLimit > 80000
```
- 그루핑된 조건들에 대해서 필터
- 그루핑된 조건 이외의 필드는 WHERE로 정렬

8. 정렬에서의 NULL

