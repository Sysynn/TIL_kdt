a, b = input('문자열을 입력하세요 > ').split()
cnt = 0
for i in a:
    if i == b:
        cnt += 1

print(cnt)
