# 15829 Hashing

import string

n = int(input())
w = input()
az = list(string.ascii_lowercase)
asc = []
for i in w:
    t = az.index(i) + 1
    asc.append(t)

res = 0
for j in range(n):
    res += asc[j] * (31 ** j)
    
print(res)