# 세로읽기
import sys, pprint

n = 15

matrix = []
sys.stdin = open("03.txt")
# for i in range(n):
#     word = list(sys.stdin.readline())
#     matrix.append(word)

# new_matrix = [[0] * n for _ in range(len(matrix))]
# result = []
# for j in range(n):
#     for k in range(len(matrix)):
#         if matrix[j][k] == None:
#             new_matrix[j][k] = " "
#         else:
#             new_matrix[j][k] = matrix[k][j]
#             result.append(new_matrix[j][k])

# res = ''.join(s for s in result)

# pprint.pp(matrix)

# # # 세로읽기



# matrix = []
# for i in range(15):
#     word = list(sys.stdin.readline())
#     matrix.append(word)

# m = len(matrix)
# n = len(max(matrix, key=len))

# new_matrix = [[0] * n for _ in range(m)]
# result = []
# for j in range(n):
#     for k in range(m):
#         if j < len(matrix[k]):
#             new_matrix[j][k] = matrix[k][j]
#             result.append(new_matrix[j][k])

# res = ''.join(s for s in result)

words = []
for i in range(5):
    words.append(sys.stdin.readline())

length = max(len(word) for word in words)

result = ''
for j in range(length):
    for word in words:
        if j < len(word):
            result += word[j]

print(result)
