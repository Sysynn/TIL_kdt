word = input('문자열을 입력하세요 > ')
d = {}
for i in word:
    if i not in d:
        d[i] = 0
    d[i] += 1

for key, value in d.items():
    print(key, value)
