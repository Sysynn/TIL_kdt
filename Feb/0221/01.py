import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
d = deque()
for t in range(0, T):
    word = input().rstrip().split()
    if word[0] == 'push_front':
        d.appendleft(word[1])
    elif word[0] == 'push_back':
        d.append(word[1])
    elif word[0] == 'pop_front':
        if len(d) < 1:
            print('-1')
        else:
            print(d[0])
            d.popleft()
    elif word[0] == 'pop_back':
        if len(d) < 1:
            print('-1')
        else:
            print(d[-1])
            d.pop()
    elif word[0] == 'size':
        print(len(d))
    elif word[0] == 'empty':
        if len(d) == 0:
            print('1')
        else:
            print('0')
    elif word[0] == 'front':
        if len(d) == 0:
            print('-1')
        else:
            print(d[0])
    elif word[0] == 'back':
        if len(d) == 0:
            print('-1')
        else:
            print(d[-1])