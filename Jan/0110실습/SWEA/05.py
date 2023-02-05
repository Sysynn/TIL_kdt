T = int(input())
for t in range(1, T+1):
    if 0 <= t <= 10000:
        numbers = list(map(int,input().split()))
        print("#{} {}".format(t, max(numbers)))
        
