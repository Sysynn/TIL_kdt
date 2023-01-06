# 전화번호부
# 키 - 이름(상호명)
# 값 - 전화번호
phone_book = {
   '전화번호': '114',
   '피자헛': '15885588',
   '김탁희': '01012331233',
   '대리운전': '15771577'
}
# print(phone_book['피자헛'])

for name in phone_book:
    #키 순회
    print(name)
    #값 순회
    print(phone_book[name])
    

# 1. 모듈을 가져오는 것!
import random

menu = ['햄버거', '피자', '초밥']
print(random.choice(menu))
# 시퀀스 내의 요소 하나를 랜덤으로 반환

# random.sample(population, k)
# Return a k length list 
# the population sequence. 1~45개 숫자 중
 