word = input('문자열을 입력해주세요 > ')
pos = 0
for i in range(len(word)):
    if word[i] == 'e':
        pos += i
        break
if pos == 0:
    print(-1)
else:
    print(pos)

    