T = int(input())
n_sums = []
for i in range(1, T + 1):
    nums = list(map(int, input().split()))
    n_sum = sum(num for num in nums if num % 2 == 1)
    n_sums.append(n_sum)

for n in range(1, T + 1):
    print(f'#{n} {n_sums[n - 1]}')