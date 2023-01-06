chars = input('문자열을 입력하세요 > ')
chars_reverse = ''

for char in chars:
    chars_reverse = str(char) + str(chars_reverse)
for idx in range(len(chars_reverse)):
    print(chars_reverse[idx])