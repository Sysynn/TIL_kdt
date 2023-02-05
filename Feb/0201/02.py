# 블랙잭

n, m = map(int,input().split())
cards = list(map(int,input().split()))
target = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]
            if target < total <=m:
                target = total            
            if total == m:
                target = m

print(target)