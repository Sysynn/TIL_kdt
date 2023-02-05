# 2525 오븐 시계

a, b = list(map(int, input().split()))
c = int(input())
d = b + c # 증가하는 분
e = d // 60 # 증가되는 시간 
if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 1000:
    if a + e <= 23 and d <= 59:
        print(a, d)
    elif a + e <= 23 and d > 59:
        print(a + e, d - 60 * e)
    else:
        print(a + e - 24, d - 60 * e)
        