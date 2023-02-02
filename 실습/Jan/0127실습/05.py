# 1181 단어 정렬

import sys

words = set() # 단어들을 저장할 빈 set 생성
for i in range(int(input())):
    word = sys.stdin.readline().strip() 
    words.add(word) # 입력값을 중복 없이 빈 set으로 add

words = list(words) # sort를 하기 위해 set을 list로 바꿈
words.sort(key=lambda x: (len(x), x)) # lambda 함수로 (len(x) 길이를 우선, 그리고 x, 사전순을 동시에 만족시키는 정렬)
                                      # words.sort(key = len(x)), words.sort() 두 개로 따로하면 앞의 조건을 만족시킨 것을
                                      # 두번쨰 정렬에서 무시하고 재정렬함... 

for word in words:
    print(word)