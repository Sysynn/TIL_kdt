#10809 알파벳 찾기

word = input()

def first_occurrence(word):
    result = [-1]*26 # 각 알파벳마다 첫 등장 위치를 저장할 리스트, 초기값은 -1로 설정
    for i in range(len(word)):
        if result[ord(word[i])-ord('a')] == -1: # 해당 알파벳이 처음 등장하는 경우
            result[ord(word[i])-ord('a')] = i
    for i in result:
        print(i, end=' ')

first_occurrence(word)
