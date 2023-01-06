# 모듈과 예외처리
#### 자료를 효율적으로 저장할 수 있을까 에 대한 고민에서 시작된 것이 데이터 저장 타입 종류가 많아졌다.
## 컨테이너 분류
### 시퀀스
- 문자열(immutatble) : 문자들의 나열
- 리스트 (mutable) : 변경 가능한 값들의 나열
- 튜플(immutable) : 변경 불가능한 값들의 나열
- 레인지 (immutable) : 숫자의 나열
### 컬렉션 / 비시퀀스
- 세트(mutable) : 유일한 값들의 모음
- 딕셔너리(mutable) : 키 - 값들의 모음

## 딕셔너리 (Dictionary)
- 키와 값 (key - value) 쌍으로 이뤄진 모음 
 - 키(key)
    - 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함)
 - 값(values)
    - 어떤 형태든 상관이 없음
- 키와 값은 : 로 구분된다. 개별 요소는 , 로 구분된다
- 변경 가능(mutable)하며 반복 가능(iterable)함

```
# 전화번호부
# 키 - 이름(상호명)
# 값 - 전화번호
phone_book = {
   '전화번호': '114',
   '피자헛': '15885588',
   '김탁희': '010-1233-1233'
   '대리운전' : '1577-1577'
}

print(phone_book['피자헛'])
```

### 딕셔너리(Dictionary) 키 - 값 추가 및 변경
- 딕셔너리에 키와 값의 쌍을 추가할 수 있으며,
이미 해당하는 키가 있다면 기존 값이 변경됨니다.

```

student = {'홍길동' : 100, ' 김철수' : 90}
students['홍길동'] = 80
# {'홍길동' : 80, '김철수' : 90}
students['박영희'] = 95

```


# 모듈
- 다양한 기능을 하나의 파일로 -> 모듈
- 다양한 파일을 하나의 폴더로 -> 패키지
- 다양한 패키질ㄹ 하나의 묶음으로 -> 라이브러리
- 이것을 관리하는 관리자 -> pip

## 모듈
- 모듈 
   - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
   - 특정 기능과 관련된 여러 모듈의 집합
   - 패키지 안에는 또 다른 서브 패키지를 포함

## 파이썬 표준 라이브러리
- 파이썬에 기본적으로 설치된 모듈과 내장함수
### random
```
import random

menu = ['햄버거', '피자', '초밥']
print(random.choice(menu))
```
 - 메뉴 안에서 요소를 선택해준다
```
import random
num = list(range(1, 46)
print(random.sample(num, 6))
```
 - 로또 추첨 코드
```
numbers = range(1, 46)
lucky_numbers = random.sample(numbers, 6)
print(sorted(lucky_numbers))
```
-> 순서대로 정렬해서 출력
```
print(sorted(random.sample(range(1,46), 6)))
```
-> 한줄로 해결
````
for i in range(5):
    numbers = range(1, 46)
    lucky_numbers = random.sample(numbers, 6)
print(sorted(lucky_numbers))
````
-> 5번 돌린다

## 메서드와 함수
### .sort() : 메서드
### return : None
### 해당 리스트 자체를 정렬!
```
number = [10, 2, 5]
result = numbers.sort()
print(result) # None
print(numbers)
=========================
number = [10, 2, 5]
result = sorted(numbers)
print(result) # [2, 5, 10]
print(numbers)
```
### Shuffle
```
students = ['민욱', '홍엽', '현석', '정은']
print(students)
random.shuffle(students)
print(random.shuffle)
```

### Date / Time
```
import datetime
print(datetime.datetime.now())
```
```
today = datetime.date(2023, 1, 5)
print(today)
print(type(today))
print(today.year)
print(today.day)
```
```
end = datetime.date(2023, 6, 14) 
# date -> datetime 시간까지
print(f'우리가 개발자가 되는 시간... {end - today}')
```
#### 패지키 관련 활용 기능은 나중에 ...
.
.



# 에러/예외처리
### 오류가 많이 발생하는 곳은 어디일까?
### 어느 부분을 중점적으로 봐야 할까?
-> 제어가 되는 시점, 조건/반복, 함수... 즉 '값이 변경되는 시점'

