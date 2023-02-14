# 숫자 카드
import sys

S = int(sys.stdin.readline().strip()) # 상근이가 가진 숫자 카드 수
S_num = list(map(int,sys.stdin.readline().strip().split())) # 상근이 카드에 적인 숫자들
C = int(sys.stdin.readline().strip()) # 체크할 카드 수
C_num = list(map(int,sys.stdin.readline().strip().split())) # 체크할 카드에 적힌 숫자들

# 상근이 카드에 적인 숫자들의 개수를 센다.
S_dict = {}
for i in S_num:
    if i not in S_dict:
        S_dict[i] = 1
    else:
        S_dict[i] += 1

# 체크할 카드에 적힌 숫자들의 개수를 구한다.
new = []
for i in C_num:
    if i in S_dict:
        new.append(S_dict[i])
    else:
        new.append(0)

print(*new)
