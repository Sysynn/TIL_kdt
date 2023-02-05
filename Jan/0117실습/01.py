#9085 더하기

T1 = int(input())
n_list = []

for t in range(0, T1):
    T2 = int(input())
    num = list(map(int, input().split()))
    total = sum(num)
    n_list.append(total)

for i in n_list:
    print(i)
