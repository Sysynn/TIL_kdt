n = int(input())

for i in range(1, n*3+1):
    if i > n*3:
        break
    print(i, end=' ')
    if i % 3 == 0:
        print()