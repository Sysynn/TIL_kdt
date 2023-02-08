# n = int(input())
# queue = list(range(1, n + 1))

# while len(queue) > 1:
#     print(queue.pop(0), end = " ")
#     queue.append(queue.pop(0))
# print(queue[0])

from collections import deque
n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    print(queue.popleft(), end = " " )
    queue.append(queue.popleft())

print(queue[0])