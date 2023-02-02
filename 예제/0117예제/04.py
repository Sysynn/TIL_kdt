#2562 최댓값
num_list = []
for i in range(0, 9):
    num = int(input())
    num_list.append(num)

high = max(num_list)
print(high)
print(num_list.index(high) + 1)