# 2167 2차원 배열의 합

# N, M = list(map(int,input().split()))
# mat = []
# for _ in range(N):
#     line = list(map(int,input().split()))
#     mat.append(line)

# T = int(input())
# for t in range(T):
#     i, j, x, y = list(map(int,input().split()))
#     cnt = 0
#     for a in range(i - 1, x):
#         for b in range(j - 1, y):
#             cnt += mat[a][b]
#     print(cnt)

# 네, 이 문제의 시간 복잡도는 O(NMT)이기 때문에 N, M, T이 커질수록 실행 시간이 길어질 수 있습니다. 
# 따라서 3중 for 문을 사용하지 않고도 문제를 해결할 수 있는 방법이 필요합니다.

# 이 문제를 해결하는 한 가지 방법은 "누적 합 배열"을 사용하는 것입니다. 누적 합 배열이란 각 위치까지의 누적 합을 저장한 배열을 말합니다. 
# 이를 활용하면 i, j부터 x, y까지의 합을 계산할 때, (x, y)까지의 누적 합에서 (i-1, y)와 (x, j-1)까지의 누적 합을 각각 빼주면 됩니다.

# 다음은 누적 합 배열을 사용하는 코드 예시입니다.

N, M = map(int, input().split())
mat = []
for _ in range(N):
    line = list(map(int, input().split()))
    mat.append(line)

# 누적 합 배열 만들기
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]

T = int(input())
for t in range(T):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

# 위 코드에서 dp[i][j]는 mat[0][0]부터 mat[i-1][j-1]까지의 부분합을 나타냅니다. 
# 이를 활용해 dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]을 계산하면 i, j부터 x, y까지의 합을 구할 수 있습니다. 
# 이 방법을 사용하면 3중 for 문을 사용하지 않아도 문제를 해결할 수 있으며, 시간 복잡도는 O(NM+T)로 훨씬 효율적입니다.



import io, os, sys
from itertools import accumulate


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n, m = map(int, input().split())
    a = [[0] * (m + 1)]
    for i in range(1, n + 1):
        r = accumulate(map(int, input().split()), initial=0)
        r = [p + r for p, r in zip(a[-1], r)]
        a.append(r)
    ans = []
    for _ in range(int(input())):
        i, j, x, y = map(int, input().split())    
        t, b = min(i, x) - 1, max(i, x)
        l, r = min(j, y) - 1, max(j, y)
        ans.append(a[t][l] - a[t][r] - a[b][l] + a[b][r])
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    sys.exit(main())
