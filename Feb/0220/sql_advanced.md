# SQL Advanced
- Transaction을 사용하여 데이터베이스의 일관성을 보장할 수 있다
- Trigger 를 이용하여 약간 자동화와 비슷한 역할을 하는 작동 방식 이해

# Transaction
- 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
- 지금까지는 구문의 종료 하나를 세미 콜론을 기준으로 해서 작성을 해왔는데,
 사실 복수의 구문들이 하나의 목적을 이루는 경우도 있다, 이런 경우 이런 여러 쿼리문들을 묶는 것을 
 Transaction이라고 한다.
- 근데 이 과정은 조건이 하나 있는데 다 성공하던지 혹은 다 실패하던지 해야하는 조건이 필요하다.
(한 개라도 실패하면 다 실패해서 없던 일이 되는...)

### Trnasaction 예시
- 계좌 이체 (인출 & 입금)
 - 송금 중에 알수 없는 문제로 인출에는 성공했는데 입금에 실패한다면?
 - 인출과 입금 모두 성공적으로 끝나야 거래가 최종 승인 되고
   중간에 문제가 발생한다면 거래를 처음부터 없던 일로 만들어야 함
 - 결국 함께 성공하던지 실패해야 함

# Transaction Syntax
```sql
START TRANSACTION;
state_ments;
...
[ROLLBACK::COMMIT];
```
- START TRASACTION
    - 트랜잭션 구문의 시작을 알림
- COMMIT
    - 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
- ROLLBACK
    - 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림

## Transaction 정리
- 쪼개질 수 없는 업무처리의 단위
- 전체가 수행되거나 또는 전혀 수행되지 않아야 함 (All or Nothing)
- 데이터베이스가 수행하는 전반적인 흐름을 일관성있게 하는 작업

# Triggers
- 특정 이벤트(INSERT, UPDATE, DELETE)에 대한 응답으로 자동으로 실행되는 것
- ~~ 변화가 생겼을 때 ~~ 하겠다

## Trigger Syntax
```sql
CREATE TRIGGER trigger_name
 {BEFORE::AFTER}{INSERT::UPDATE::DELETE}
 ON table_name FOR EACH ROW
 trigger_body;
 ```
 - 언제? 어디서? 트리거 코드 (~하겠다) 
 - FOR EACH ROW는 매 구문 반영하겠다 기본적으로 써준다고 생각하면 됨
- 트리거는 DML의 영향을 받는 필드값에만 적용 가능 (SELECT 같은 DQL에는 적용불가)

```sql
CREATE TRIGGER myTrigger
	-- 언제?
    BEFORE UPDATE
    ON articles FOR EACH ROW
    SET updatedAt = CURRENT_TIME();
    
```
- body가 여러개라고 하면
```sql

BEGIN
	SET updatedAt = CURRENT_TIME();
	SET updatedAt = CURRENT_TIME();
	SET updatedAt = CURRENT_TIME();    
END;
```
해야 되는데, ;가 두번 들어가서 END 앞의 ;는 앞에서 끝나버림...
어떻게 해야 저 body들을 묶어줄수 있을까?
DELIMETER // 여기서부터 종료조건은 이제 '//'다 라고 선언하는 것 
(더이상 세미콜론;이 종료조건이 아니다. 언제까지? 다음 DELIMETER가 나올때까지)
DELMITER ; <- 여기서부터는 이제 다시 ;로 변경

```sql
DELIMITER //
CREATE TRIGGER myTrigger
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
	SET updatedAt = CURRENT_TIME();
	SET updatedAt = CURRENT_TIME();
	SET updatedAt = CURRENT_TIME();    
END//
DELMITER ;
```
- 트리거가 접근하는 데이터가 전후에 어떤 값을 컨트롤하는지 명확히 하기위해서
```sql
DELIMITER //
CREATE TRIGGER myTrigger
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
	SET NEW.updatedAt = CURRENT_TIME();   
END//
DELMITER ;
```