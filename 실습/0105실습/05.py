name = input('이름을 입력하세요 > ')
phone = input('전화번호를 입력하세요 > ')
email = input('이메일을 입력하세요 > ')
home = input('거주지를 입력하세요 >')

mini_prof = {
    '전화번호': phone,
    '이메일': email,
    '거주지': home
}
prof = {
    name : mini_prof
}

print(prof)