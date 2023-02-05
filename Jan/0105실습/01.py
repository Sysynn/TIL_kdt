word = input('문자열을 입력하세요 > ')
l = list(word)
cnt = 0

for i in l:
    if i == 'e':
        cnt += 1


print(cnt)
