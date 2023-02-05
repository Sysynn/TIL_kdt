#10773 제로

number = int(input())
num_list = []
for i in range(0, number):
    num = int(input())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

print(sum(num_list))
