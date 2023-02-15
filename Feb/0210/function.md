# Function

```
def my_function(something):
 # Do this with something
 # Then do this
 # Finally do this
```
my_function() 이라고 호출 할 때 마다 위의 function을 실행
"something"에 들어갈 값은 함수 내에서 변수와 연결하는 매개변수

```
def my_funtion(): <- 빈칸으로 놔두고
    result = 3 * 2 
    return result 
```
나중에 이 함수를 호출할 때 my_funtion()을 실행하면
호출된 result 값이 my_funtion()을 대체
```
output = my_funtion()
```
이 경우 output = 6이 됨

가령, len 함수를 보면
```
output = len("ABCDE")
```
len() 은 함수이고, ()은 input이다. 이 함수가 호출되면 무엇이 되든 함수안의
return 값이 len()을 대체하고 output 변수에 저장된다는 의미이다.

# return 값을 갖는 함수
컴퓨터가 return이라는 단어를 확인하면 그 라인이 그 함수의 끝이라는 것을 인식
return이 일단 한번 들어가면 그 이후에 무슨 코드가 있든 컴퓨터는 인식하지 않는다. 
