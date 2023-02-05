a = input('문자열을 입력하세요 > ')
list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
cnt = 0

for i in a:
    if i in list:
        cnt += 1

print(cnt)