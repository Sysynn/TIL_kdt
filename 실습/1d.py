# n == 1 : [5, 1, 2, 3, 4]
# n == 2 : [4, 5, 1, 2, 3]

a = [1, 2, 3, 4, 5]
N = len(a)

n = 2
new_a = [None for _ in range(N)]
print(a, new_a)
for i in range(N):
    #새로운 리스트에
    print((i+n)%N)
    new_a[(i+n)%N] = a[i]
    print(new_a)
for n in range(5):
    print(a[-n:] + a[:-n])
    


