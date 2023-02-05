# 2576 홀수

T = 7
num_list = []
for i in range(0, T):
    num = int(input())
    num_list.append(num)

odd = []
for i in num_list:
    if i % 2 == 1:
        odd.append(i)

if sum(odd) == 0:
    print("-1")
elif sum(odd) > 0:
    print(sum(odd))
    print(min(odd))