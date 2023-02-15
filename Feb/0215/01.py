# 1065 한수

N = int(input())
res = 0

for i in range(1, N + 1):
    if i <= 99:
        res += 1
    elif int(str(N)[0]) - int(str(N)[1]) == int(str(N)[1]) - int(str(N)[2]):
            res += 1
    else:
        continue

print(res)