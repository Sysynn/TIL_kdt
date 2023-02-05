# 2846 오르막길

T = int(input())
hills = list(map(int,input().split()))            # 높이 개수 입력 받기
ups = []                                          # 연결되는 언덕의 개수를 받기 위해 빈 리스트 생성
up = 0                                            # 연결되는 언덕의 높이를 한번에 세주기 위해 초기화용 생성
for i in range(0, len(hills)):
    if i == len(hills) - 1:                       # 차수가 마지막일 때
        ups.append(up)                            # 마지막 높이를 append 하고
        break                                     # 빠져나감
    if int(hills[i]) < int(hills[i+1]):           # 차수가 다음 수보다 작으면 
        up = up + int(hills[i+1]) - int(hills[i]) # 높이에 두 수의 차를 더함
    else:                                         # 뒤 수가 더 작으면 초기화시킴
        ups.append(up)
        up = 0 
        
print(max(ups))