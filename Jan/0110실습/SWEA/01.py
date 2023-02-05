

T = int(input())

for t in range(1,T + 1):
    a, b = list(map(int,input().split()))
    s = a // b #몫 계산
    r = a % b  #나머지 계산
    print(f"#{t} {s} {r}")