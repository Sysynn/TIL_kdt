T = int(input())
answer = list(map(int,input().split()))
p_list = []
cnt = 0
for i in answer:
    if i == 1:
        cnt = cnt + 1
        p_list.append(cnt)
    else:
        p_list.append(0)
        cnt = 0
        
print(sum(p_list))