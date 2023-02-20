# 11866 요세푸스 문제 0

# N, K = list(map(int,input().split()))
# line = list(range(1,N + 1))
# new_line = []
# while len(line) > 0:
#     if len(line) < K:
#         new_line.append(line[K % len(line) - 1])
#         line.remove(line[K % len(line) - 1])
#     else:
#         new_line.append(line[K - 1])
#         line.remove(line[K - 1])
#         line = line[K - 1:len(line)] + line[0:K - 1]
# print(f"<{', '.join(str(x) for x in new_line)}>")   
    
N, K = list(map(int, input().split()))
line = list(range(1, N+1))
new_line = []

idx = K - 1
while len(line) > 0:
    new_line.append(line.pop(idx))
    if len(line) > 0:
        idx = (idx + K - 1) % len(line)

print(f"<{', '.join(str(x) for x in new_line)}>")
