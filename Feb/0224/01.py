# Codeup 6098 성실한 개미

# 현재 위치를 9로 바꾼다.
# 현재 위치가 2이면, 탐색을 종료한다.
# 오른쪽에 1이 있으면 오른쪽으로 이동하고, 1을 9로 바꾼다.
# 오른쪽에 1이 없고, 아래쪽에 1이 있으면 아래쪽으로 이동하고, 1을 9로 바꾼다.
# 오른쪽과 아래쪽 모두에 1이 없으면 탐색을 종료한다.

from pprint import pprint
import sys

sys.stdin = open('input_1.txt')

a = []
for _ in range(10):
    input_line = sys.stdin.readline().rstrip()
    mi = list(map(int,input_line.split()))
    a.append(mi)

x, y = 1, 1 # 시작 위치

while True:
    if a[x][y] == 2:  # 먹이를 찾으면
        a[x][y] = 9  # 현재 위치를 9로 표시
        break  # 반복문 종료
    a[x][y] = 9  # 지나온 자리를 9로 표시
    if a[x][y+1] != 1:  # 오른쪽으로 갈 수 있는 경우
        y += 1
    elif a[x+1][y] != 1:  # 아래쪽으로 갈 수 있는 경우
        x += 1
    else:  # 갈 수 있는 방향이 없는 경우
        break

for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()