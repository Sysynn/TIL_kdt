##2750 수 정렬하기

N = int(input())
num_list = []

for i in range(0, N):
    num = int(input())
    num_list.append(num)

sorted_list = sorted(num_list)

for x in sorted_list:
    print(x)