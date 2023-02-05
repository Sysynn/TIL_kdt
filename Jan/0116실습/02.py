a, b = list(map(int, input().split()))
c = list(map(int,input().split()))
numbers = []
for i in c:
    if b > i:
        numbers.append(i)

print(*numbers)