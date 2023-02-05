# 10817 세 수
# import sys, heapq
# input = sys.stdin.readline
# heapq.heapify(input)

import heapq

numbers = list(map(int,input().split()))
heapq.heapify(numbers)
heapq.heappop(numbers)

print(numbers[0])

