#11720 숫자의 합
N = int(input())
numbers_str = input()
numbers = [int(num) for num in numbers_str]
total = 0
for num in numbers:
    total += num
print(total)