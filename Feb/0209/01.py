# 2605 줄 세우기

num = int(input())
lunch_q = list(map(int,input().split()))
new_q = []
for i in range(1, len(lunch_q) + 1):
    new_q.insert(len(new_q) - lunch_q[i - 1], len(new_q) + 1)
print(*new_q)
