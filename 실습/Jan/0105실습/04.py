name = input('이름을 입력하세요 > ')
phone = input('전화번호를 입력하세요 > ')
home = input('거주지를 입력하세요 > ')
dict_variable = {'이름': name, '전화번호': phone, '거주지': home}
for key in dict_variable:
    print(key, ':', dict_variable[key])