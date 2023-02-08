# SWEA 2001 파리 퇴치

T = int(input())
for t in range(1, T + 1):    
    N, M = list(map(int, input().split()))
    matrix = []
    for n in range(N):
        line = list(map(int,input().split()))
        matrix.append(line)


    temp = []

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            flies = 0
            for d in range(M):
                for s in range(M):
                    flies += matrix[i+d][j+s]
            temp.append(flies)

    killed = max(temp)
    print(f"#{t} {killed}")

