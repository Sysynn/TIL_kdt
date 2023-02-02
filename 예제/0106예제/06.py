n = int(input())
inputs = [list(map(int, input().split())) for _ in range(n)]

for i, (a, b) in enumerate(inputs):
    print("Case #{}: {} + {} = {}".format(i+1, a, b, a + b))