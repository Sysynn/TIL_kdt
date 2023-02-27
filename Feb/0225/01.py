# SWEA 1954 달팽이 숫자

#  우 하 좌 상 순서로 가는 것 => if를 네개로 만들어야하나?
# 행 또는 열 끝까지 다달았을때 회전

N = 3
dal = [[0] * N for _ in range(N)]
lot = 0         # 방향 회전 횟수
x = 0 
y = 0
corner = 1 + (N - 1) * lot # 꼭짓점
for i in range(0, N ** 2):
    if y < N:
        y += 1
        dal[x][y] = i + 1   
        
    elif y >= N:
        x += 1
        dal[x][y] = i + 1
    


# # 입력 받기
# n = int(input())

# # 2차원 배열 초기화
# arr = [[0] * n for _ in range(n)]

# # 이동 방향 설정 (오른쪽, 아래쪽, 왼쪽, 위쪽 순서)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# # 초기 위치 및 숫자 설정
# x, y = 0, 0
# num = 1

# # 달팽이 모양으로 숫자 채우기
# for i in range(n * n):
#     arr[x][y] = num
#     num += 1

#     # 다음 위치 찾기
#     nx, ny = x + dx[i // n % 4], y + dy[i // n % 4]

#     # 다음 위치가 배열 범위를 벗어나거나 이미 채운 위치인 경우 방향 전환
#     if not 0 <= nx < n or not 0 <= ny < n or arr[nx][ny] != 0:
#         x, y = x + dx[(i // n % 4 + 1) % 4], y + dy[(i // n % 4 + 1) % 4]
#     else:
#         x, y = nx, ny

# # 결과 출력
# for row in arr:
#     print(*row)
