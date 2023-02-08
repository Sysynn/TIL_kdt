import sys

A, B, C = list(map(int,sys.stdin.readline().split()))


if B >= C:
    print("-1")
else:
    D = A // (C - B) + 1
    print(D)