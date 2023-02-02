T = int(input())
for t in range(1, T+1):
    nums = list(map(int, input().split()))
    average = sum(nums) / len(nums)
    average = round(average)
    print("#{} {}".format(t,average))
