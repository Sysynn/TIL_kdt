# 1065 한수

N = int(input())
res = 0

for i in range(1, N + 1):
    if i <= 99:
        res += 1
    elif int(str(i)[0]) > int(str(i)[1]):
        if int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
            res += 1
        else:
            continue
    elif int(str(i)[0]) < int(str(i)[1]):
        if int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
            res += 1
        else:
            continue
    elif int(str(i)[0]) == int(str(i)[1]):
        if int(str(i)[1]) == int(str(i)[2]):
            res += 1
        else:
            continue
    else:
        continue

print(res)  