# 2167 2차원 배열의 합

N, M = list(map(int,input().split()))
mat = []
for _ in range(N):
    line = list(map(int,input().split()))
    mat.append(line)

T = int(input())
for t in range(T):
    i, j, x, y = list(map(int,input().split()))
    cnt = 0
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            cnt += mat[a][b]
    print(cnt)
