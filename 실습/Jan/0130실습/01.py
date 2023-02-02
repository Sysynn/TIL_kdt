# 1225 이상한 곱셈

A, B = input().split()
list_A = list(A)
list_B = list(B)
total = 0
for i in list_A:
    for j in list_B:
        total = total + int(i) * int(j)

print(total)

A, B = input().split()
row1 = [int(x) for x in A]
row2 = [int(x) for x in B]
result = 0

A, B = map(int, input().split())
print(sum(map(int, str(A))) * sum(map(int, str(B))))
