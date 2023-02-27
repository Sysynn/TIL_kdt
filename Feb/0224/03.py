# Codeup 6096 바둑알 십자 뒤집기
import sys

sys.stdin = open('input_3.txt')

d = [] # 바둑판 생성
for _ in range(19): # 0부터 18까지 19개의 바둑알
    input_line = sys.stdin.readline().rstrip() 
    mi = list(map(int,input_line.split())) # 리스트로 받아서
    d.append(mi) # 바둑판에 저장
    
n = int(sys.stdin.readline().rstrip()) # 시도 회수
for i in range(n) : 
  x,y=list(map(int,sys.stdin.readline().rstrip().split())) # 기준이 되는 위치
  for j in range(1, 20) : # 1부터 19까지 19개의 바둑알
    if d[x-1][j-1]==0 : # 바둑판상 좌표 (x-1, y-1)를 기준으로 가로로 한 줄을 탐색하면서 0이면
      d[x-1][j-1]=1 # 해당 바둑알을 뒤집어 1로 만들고
    else : # 반대의 경우면
      d[x-1][j-1]=0 # 역시 뒤집어서 0으로 만듬

    if d[j-1][y-1]==0 : # 세로로 한 줄을 탐색하면서 같은 작업 반복
      d[j-1][y-1]=1
    else :
      d[j-1][y-1]=0

      
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()