#3052 나머지

# li = []
# for i in range(0,10):
#     num = int(input())
#     res = num % 42
#     li.append(res)

# result = set(li)

# print(len(result))

import sys

li = []
for i in range(0,10):
    num = int(sys.stdin.readline())
    res = num % 42
    li.append(res)

result = set(li)

print(len(result))