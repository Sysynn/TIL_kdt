# # #3009 네 번째 점

hor = []
ver = []
for point in range(0, 3):
    a, b = list(map(int,input().split()))
    hor.append(a)
    ver.append(b)

last_point = [x for x in hor if hor.count(x) == 1] + [y for y in ver if ver.count(y) == 1]
print(*last_point)


