# 1966 프린터 큐

# T = int(input())
# for t in range(0, T):
#     N, M = list(map(int,input().split()))
#     docs = list(map(int,input().split()))
#     cnt = 0
#     while len(docs) > 0:
#         if len(docs[:M+1]) == len(docs):
#             cnt += 1
#             break
#         elif docs[-1] != max(docs):
#             cnt += 1
#             docs.pop()
#         else:
#             docs.pop()
#     print(cnt)

T = int(input())
for t in range(0, T):
    N, M = list(map(int,input().split()))
    docs = list(map(int,input().split()))
    printer = []  
    cnt = 0
    for i in range(0, N):
        pair = [0, 0]
        pair[0] = i
        pair[1] = docs[i]
        printer.append(pair)
    while len(printer) > 0:
        if len(printer) == 1:
            cnt += 1
            break
        elif printer[0][1] == max(docs):
            cnt += 1
            if printer[0][0] == M:
                break
            else:
                printer.remove(printer[0])
                docs.remove(max(docs))
        else:
            printer.append(printer[0])
            printer.remove(printer[0])
    print(cnt)