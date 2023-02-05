# 2441 별찍기 - 4

N = int(input())

for i in range(N):
    print(" " * (N - (N - i)) + "*" * (N - i))
    