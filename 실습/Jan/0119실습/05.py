# 2577 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

sum = A * B * C
string = str(sum)

cnt = []
for i in range(1, 10):
    cnt.append(string.count(str(i)))


print(string.count(str(0)))    
for i in cnt:
    print(i)
    