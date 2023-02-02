T = int(input())
c = {}
for t in range(0, T):
    a, b = list(map(int, input().split()))
    c[t + 1] = a + b


for x in c:
    print(f"Case #{x}: {c[x]}")