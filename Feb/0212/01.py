# 4673 셀프 넘버
def d(num):
    tot = 0
    for i in str(num):
        tot += int(i)
    result = num + tot
    return result

a = []
for i in range(1, 10000):
    n = d(i)
    if n <= 10000:
        a.append(n)
b = sorted(a)
c = list(range(1,10001))
d = list(set(c) - set(b))
e = sorted(d)
for j in e:
    print(j)