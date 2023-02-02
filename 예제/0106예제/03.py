T = int(input())
c = list()
for t in range(0, T):
    a, b = list(map(int, input().split()))
    c.append(a + b)

for x in c:
    print(x)