# 1547 공

T = int(input())

with_ball = 1 # 공은 처음에 1번 위치에 들어있다

for i in range(0, T):    
    a, b = list(map(int,input().split())) # a, b 두 컵을 선택한다
    if a == with_ball: # 만약 첫번째 선택한 컵이 공의 위치라면
        with_ball = b  # 선택한 다른 컵이 공의 위치로 이동한다
    elif b == with_ball:
        with_ball = a

print(with_ball)
        
