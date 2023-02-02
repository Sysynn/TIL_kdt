#1. 손수 만들기
# matrix = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
# ]

# 2. for 문 활용
# print([0] * 10)
# 4X3 행렬 만든다고 하면
N = 4 #행
M = 3 #열

matrix = []
for _ in range(N):
    #[0, 0, 0, 0, ... 0]
    matrix.append([0] * M)

import pprint
pprint.pprint(matrix)

matrix = [[0] * M] * N
print(matrix)
matrix[0][0] = 1
print(matrix)
print("---------------")
matrix2 = [[0] * M for _ in range(N)]
print(matrix2)
matrix2[0][0] = 1
print(matrix2)

#리스트 컴프리헨션으로 이차원 만드는 예시
list_2d_1 = [[0] * (10**4) for _ in range(10**4)]
print(len(list_2d_1), len(list_2d_1[0]))

#순수 for
list_2d_2 = []

for _ in range(10**4):
    row = [0] * (10 ** 4)
    list_2d_2.append(row)
    
print(len(list_2d_2), len(list_2d_2[0]))