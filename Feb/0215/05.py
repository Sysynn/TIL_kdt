# 2869 달팽이는 올라가고 싶다

a, b, c = list(map(int,input().split()))
if a >= c:
    print(1)
else:
    cnt = ((c-a) // (a-b)) + 1
    if (c-a) % (a-b) != 0:
        cnt += 1
    print(cnt)