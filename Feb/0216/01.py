# 2775 부녀회장이 될테야

T = int(input())
for t in range(T):
    k = int(input()) # 층수
    n = int(input()) # 호수
    floor = [x for x in range (1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]
    print(floor[-1])