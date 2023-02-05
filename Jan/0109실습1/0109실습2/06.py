n = int(input('양의 정수를 입력하세요 >'))
sum = 0
while n > 0 :
    sum += n % 10
    n //= 10
if n >= 0:
    print(sum)
else:
    print(-1)