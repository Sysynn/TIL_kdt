# 4153 직각 삼각형

while True:
    lines = list(map(int,input().split()))
    if lines == [0, 0, 0]:
        break
    l = sorted(lines)    
    if l[2] ** 2 == l[0] ** 2 + l[1] ** 2:
        print("right")
    else:
        print("wrong")