# 10989 수 정렬하기 3
import sys
input = sys.stdin.readline
T = int(input())
li = [0] * 10001
for t in range(T):
    num = int(input())
    li[num] += 1

for i in range(0, 10001):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)
