# 1526 가장 큰 금민수

# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

N = int(input()) # 숫자열로 입력을 받는다
target = N # 목표 숫자

while True: # while문을 사용해서 각 자리수에 4와 7의 개수가 자릿수와 같다면 조건에 맞다고 봄
   if len(str(target)) == str(target).count("4") + str(target).count("7"): # 자릿수가 4의 개수, 7의 개수의 합과 같다면
       print(target) # 목표 숫자 출력
       break
   target -= 1 # 될 때까지 목표숫자에서 1씩 깎는다
        