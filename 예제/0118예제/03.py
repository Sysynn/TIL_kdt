# # 펠린드롬인지 확인하기

# word = input()

# word_reverse = word[::-1]

# if word == word_reverse:
#     print("1")
# else:
#     print("0")



# 1. Input
word = 'level'

# 2. 값 초기화(단어의 인덱스)
# start(시작) : 0
# end(Rmx) : len(word) - 1
start = 0
end = len(word) - 1
is_pal = True # 펠린드롬인지 아닌지 확인

# 3. while
# start 값이 end 보다 작을 때...
while start < end:
    # word[start], word[end] 비교해서
    # 다르면, 펠린드롬이 아니다!
    if word[start] != word[end]:
        is_pal = False
        break
    # 매 반복이 끝나면
    # start는 1씩 증가하고
    # end는 1씩 감소
    start += 1
    end -= 1
    
# 4. 출력
# 펠린드롬이면 1, 아니면 0 을 출력한다
if is_pal == 1:
    print(1)
else:
    print(0)