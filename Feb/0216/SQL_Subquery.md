# Subquery
- 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는데 사용
- SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용

## Subquery 예시
- table 1 에서 가장 나이가 어린 사람을 삭제해야 하면?
```sql
DELETE FROM table1
WHERE age = (
    SELECT MIN(age) FROM table1
);
```
한번에 가장 많은 돈을 소비한 고객 번호를 조회하려면
```sql
SELECT customerNumber, amount
FROM payments
WHERE amount = (
    SELECT MAX(amount)
    FROM payments
);
```

- 미국에 있는 사무실에서 근무하는 직원의 이름과 성 조회
 1. 미국에 사무실에서 일하는 직원과 이름과 성 조회
 2. 미국 사무실 코드를 가지고 있는 목록
 3. 직원 테이블의 officecode가 1,2,3 인지 확인

 이 과정을 코드로 옮기면

```sql
SELECT lastName, firstName
FROM employees
WHERE officeCode IN
(SELECT officeCode
 FROM offices
 WHERE country = 'USA'
);
```
- 주문한 적이 없는 고객 목록 조회
1. orders에는 주문한 고객들만 들어있음 -> NOT IN
2. [orders에서 고객 목록]을 가져와서
3. [고객 테이블의 모든 정보]와 위에서 가져온 고객 주문 목록을 비교
4. 결국 위에서 가져온 고객 주문 목록에 포함되지 않는 고객이 범인
```sql
SELECT customerName
FROM customers
WHERE customerNumber NOT IN
  (SELECT DISTINCT customerNumber
  FROM orders
  );
```


- FROM에 붙은 파생된 테이블에는 항상 이름을 지정해줘야 함


# EXISTS
- WHERE절에서 subquery의 결과가 있는지 없는지를 판단하는 역할

```sql
SELECT employeeNumber, firstName, lastName
FROM employees
WHERE EXISTS(
	SELECT *
    FROM offices
    WHERE
		city = 'Paris' AND employees.officeCode = offices.officeCode
```

# CASE
```sql
CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value2 THEN statements
    ...
    [ELSE else_statements]
END CASE;
```
- case_value 가 when_value와 동일한 것을 찾을때까지 순차적으로 비교
- 조건문이기 때문에 else가 있지만 없을수도 있음
- when_value 와 case_value를 찾으면 해당 THEN 절의 코드를 실행


HackerRank 웹사이트 참조