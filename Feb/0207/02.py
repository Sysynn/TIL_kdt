# 7568 덩치
T = int(input()) # 테스트 케이스 개수
height = [] # 몸무게 리스트
weight = [] # 키 리스트
body = []
bigger = []

for t in range(T):
    a, b = list(map(int,input().split())) 
    body.append([a, b])

