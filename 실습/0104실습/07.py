number_list = [1, 2, 3, 4, 5]
sm_number = number_list[0]
for number in number_list[1:]:
    if number < sm_number:
        sm_number = number
print(sm_number)