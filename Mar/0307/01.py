import sys

N, M = list(map(int,sys.stdin.readline().rstrip().split()))
box = []
for n in range(1, N+1):
    box.append(n)

for m in range(0, M):
    i, j = list(map(int,sys.stdin.readline().rstrip().split()))
    box[i-1], box[j-1] = box[j-1], box[i-1]

print(*box)
