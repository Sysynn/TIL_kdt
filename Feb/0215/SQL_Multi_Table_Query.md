# SQL - Multi Table Queries
- 관계형 데이터베이스에서 외래 키 필드 역할 학습
- JOIN 키워드 (세 가지)
- 여러 개의 다른 테이블들을 연결지어 출력

# JOINING TABLE
## JOIN clause
- 둘 이상의 테이블에서 데이터를 검색하는 방법
## JOIN 종류
1. INNER JOIN
2. OUTER JOIN
 - LEFT JOIN
 - RIGHT JOIN
3. CROSS JOIN

## INNER JOIN clause
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
```sql
SELECT
  select_list
FROM
  table1
INNER JOIN table2
  ON table1.fk = table2.pk;
```
기준이 되는 테이블을 선택하고 조인되서 붙는 테이블을 그 다음에 작성
어떤 조건에 맞춰서 할거냐? ON 을 써서...
위 예를 보면 테이블1의 외래키와 테이블2의 프라이머리 키를 조인한다.
메인이 되는 테이블의 키와 조인할 테이블의 프라이머리키가 붙어서 출력된다. 
(다른 테이블의 정보도 같이 불러온다)
```sql
SELECT *
FROM articles
INNER JOIN users
```
위 코드에서는 *를 써서 모두 불러왔지만 필요한 부분만 보고 싶을 때는
SELECT  id, title, content, name
FROM articles
INNER JOIN users
과 같이 선택해서 출력 가능
그런데 만약 위 코드에서 id 필드가 여러 테이블에 중복되어 존재하는 경우에는
앞에 테이블이름을 명확하게 붙여주면 된다. (예를들면 articles.id)

## LEFT JOIN
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드를 반환
- 왼쪽 테이블은 비교할거 없이 일단 다 출력, 그리고 오른쪽 테이블에 레코드가 없는 부분은 NULL로 출력
```sql
SELECT
  select_list
FROM
  table1
LEFT [OUTER] JOIN table2
  ON table2.fk = table2.pk;
```

## RIGHT JOIN
- 왼쪽 테이블과 일치하는 레코드와 함께 오른쪽 테입르은 모두 반환
- 왼쪽 테이블에 일치하는 레코드가 없을 경우 NULL로 출력
- FROM 에 있는게 무조건 왼쪽

SQL Join Visualizer 를 통해서 비교가능
