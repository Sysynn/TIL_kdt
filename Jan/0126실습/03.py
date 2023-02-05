#1453 피시방 알바

customers = int(input())
seats = list(map(int,input().split()))
S = set(seats)
A = len(seats) - len(S)
print(A)