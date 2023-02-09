# 덩치
T = int(input())
size = []
for t in range(T):
    x, y = list(map(int,input().split()))
    size.append([x, y])
    
rank = []

for s in range(T):
    cnt = 1
    stan1 = size[s][0]
    stan2 = size[s][1]
    for i in range(len(size)):
        if size[i][0] > stan1:
            if size[i][1] > stan2:
                cnt += 1
    
    rank.append(cnt)
    
print(*rank)