# N, M = list(map(int,input().split()))
# li = [0] * N


# for m in range(0, M):
#     x, y, num = list(map(int,input().split()))
#     li[x-1:y] = [num] * (y-x+1)
    
# print(*li)

N, M = list(map(int,input().split()))
print(N//M)
print(N%M)