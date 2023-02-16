# 10250 ACM 호텔
T = int(input())

for i in range(T):
    h, w, n = map(int, input().split( ))

    floor = n % h 
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)


# f-string f'{num:02}' 를 사용하면 0을 포함하는 두자리 수로 출력 가능