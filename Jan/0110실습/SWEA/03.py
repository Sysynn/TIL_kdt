a, b = list(map(int,input().split()))
if 0 <= a <= 9 and 0 <= b <= 9:
    print((a+b)//1)
    print((a-b)//1)
    print((a*b)//1)
    print(int((a/b)//1))