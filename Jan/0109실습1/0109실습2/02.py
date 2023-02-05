s = input('문자열을 입력하세요 > ')
words = s.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

for key, value in counts.items():
    print(f"{key} {value}")