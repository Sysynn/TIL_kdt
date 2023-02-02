#2669 직사각형 네개의 합집합의 면적 구하기
# w = [[0]*100 for _ in range(100)]
# cnt = 0
# for _ in range(4):
#     x1, y1, x2, y2 = map(int,input().split())
#     for i in range(x1,x2):
#         for j in range(y1,y2):
#             if w[i][j] ==0:
#                 w[i][j]=1
#                 cnt +=1
# print(cnt)


import sys
sys.stdin = open("input.txt")

# 101*101 이차원 리스트
graph = []

# 시작 인덱스 -> 0
# 마지막 인덱스 -> 0
for _ in range(101):
    temp = [0] * 101
    graph.append(temp)

# 입력 줄 수

N = 4

for _ in range(N):
    number_list = input().split()
    
    x1 = int(number_list[0])
    y1 = int(number_list[1])
    x2 = int(number_list[2])
    y2 = int(number_list[3])
    print(x1, y1, x2, y2)

    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1
print(graph)