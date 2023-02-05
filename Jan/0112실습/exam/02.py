T = int(input())
results = []
for t in range(1, T+1):
    date = input()
    year = date[0]+date[1]+date[2]+date[3]
    mon = date[4]+date[5]
    day = date[6]+date[7]
    if (int(mon) > 12 or int(day) > 31) or (int(mon) < 1 or int(day) < 1) or ((int(mon) == 4 or int(mon) == 6 or int(mon) == 9 or int(mon) == 11) and int(day) >30) or (int(mon) == 2 and int(day) > 28):
        results.append(f'#{t} {-1}')
    else:
        results.append(f'#{t} {year}/{mon}/{day}')
for result in results:
        print(result)