# Codeup 6097 설탕과자 뽑기
import sys

sys.stdin = open('input_2.txt')
h, w = list(map(int,sys.stdin.readline().rstrip().split())) # 격자판의 가로 세로
n = int(sys.stdin.readline().rstrip()) # 막대의 수
table = [[0 for _ in range(w)] for _ in range(h)] # 격자판 생성
for _ in range(n): # 막대의 수 만큼
    l, d, x, y = list(map(int,sys.stdin.readline().rstrip().split())) #막대의 길이, 방향, 시작 위치
    x -= 1
    y -= 1
    if d == 0: # 방향이 가로면
        for j in range(y, y + l): # 가로로 막대 길이만큼
            table[x][j] = 1
    else: # 방향이 세로면
        for i in range(x, x + l): # 세로로 막대 길이만큼
            table[i][y] = 1
for i in range(h):
    for j in range(w):
        print(table[i][j], end=' ')
    print()