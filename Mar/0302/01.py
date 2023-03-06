# 2511 카드놀이

import sys

sys.stdin = open('input.txt')
A_line = list(map(int,sys.stdin.readline().rstrip().split()))
B_line = list(map(int,sys.stdin.readline().rstrip().split()))
A = 0
B = 0
winner = []
last_win = 'D'
for i in range(0, len(A_line)):
    if A_line[i] > B_line[i]:
        A += 3
        last_win = 'A'
    elif A_line[i] < B_line[i]:
        B += 3
        last_win = 'B'
    elif A_line[i] == B_line[i]:
        A += 1
        B += 1

if A > B:
    winner.append('A')
elif A < B:
    winner.append('B')
else:
    winner.append(last_win)
print(A, B)
print(*winner)
