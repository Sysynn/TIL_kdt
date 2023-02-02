numbers = []
for i in range(5):
    x = int(input())
    if x < 40:
        x = 40
    numbers.append(x)

average = sum(numbers) / 5
print(int(average))