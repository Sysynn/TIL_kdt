number_list = [1, 2, 3, 4, 5]
largest_number = number_list[0]
for number in number_list[1:]:
    if number > largest_number:
        largest_number = number
print(largest_number)