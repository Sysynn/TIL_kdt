# 2455 지능형 기차
intrain = 0
max_no = 0
for i in range(0, 4):
    a, b = list(map(int, input().split()))
    intrain = intrain - a + b
    if intrain > max_no:
        max_no = intrain

print(max_no)