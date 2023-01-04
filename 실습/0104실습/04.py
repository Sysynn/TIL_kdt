number_list = [2, 10, 12, 1823]
pos = 0 
total = 0

for i in number_list: 
    pos += 1
for number in number_list:
    total += number

print(total/pos)