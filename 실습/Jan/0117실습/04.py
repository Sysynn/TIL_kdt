#10952 A + B - 5

total = []
while True:
    a, b = list(map(int, input().split()))   
    if a == 0 and b == 0:
        break
    total.append(a + b)
    
for num in total:
    print(num)