import sys

T = int(sys.stdin.readline()) # 테스트 케이스
cols = [] # 기둥 리스트
start = 0 # 기둥 높이
for t in range(0, T): # 테스트 케이스만큼 순회
    col = int(sys.stdin.readline()) # 기둥 높이 입력
    cols.append(col) #기둥리스트에 append
vis = cols[::-1]
high = 0
cnt = 0
for v in vis:
    if v > high:
        high = v
        cnt +=1
        
print(cnt)