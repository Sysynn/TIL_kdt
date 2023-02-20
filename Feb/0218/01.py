# 2291 벌집

T = int(input())
cnt = 1
if T == 1:
    print("1")
else:
    for i in range(0, T + 1):
        cnt += 6 * i
        if cnt >= T:
            break
        else:
            continue
    print(i + 1)