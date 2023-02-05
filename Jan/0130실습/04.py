#2953 나는 요리사다

matrix = [list(map(int, input().split())) for _ in range(5)]
scores = []
for i in matrix:
    scores.append(sum(i))

top = max(scores)
winner = []
for j in scores:
    if j == top:
        winner.append(scores.index(j) + 1)    
print(*winner, top)

# dict = {} # 딕셔너리
# for i in range(1,6):
#     a = map(int,input().split())
#     dict[i]= sum(a)
# print(max(dict, key=dict.get),max(dict.values()))
# max(dict,key=dict.get) (최대 벨류값의 키값 불러오기)
# max(dict.values()) (최대 벨류값 출력)