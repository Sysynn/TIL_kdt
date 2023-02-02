#2675 문자열 반복

T = int(input())
result = []
for i in range(0, T):
    num, word = input().split()
    part = [i*int(num) for i in word]
    result.append("".join(part))

for i in range(T):
    print(result[i])