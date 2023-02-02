s = input('문자열을 입력하세요 > ')
lst = [char for char in s if char != 'e']
print(''.join(lst))