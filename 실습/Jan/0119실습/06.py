# 7785 회사에 있는 사람
import sys

T = int(input())
set_list = set()
for i in range(0, T):
    name, action = sys.stdin.readline().split()
    if action == "enter":
        set_list.add(name)
    else:
        set_list.discard(name)
set_list = list(set_list)
set_list.sort()
set_list.reverse()

for i in set_list:
     print(i)