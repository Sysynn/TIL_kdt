# 2606 바이러스

n = int(input()) # 컴퓨터 개수
m = int(input()) # 네트워크 개수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
total = 0

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start] # 돌아갈 곳을 기록
    visited[start] = True # 시작 정점 방문 처리
    while stack: # 스택이 빌 때까지 (돌아갈 곳이 없을때까지) 반복
        cur = stack.pop() # 현재 방문 정접(후입선출)
        
        for adj in graph[cur]: # 인접한 모든 정점에 대해
            if not visited[adj]: #아직 방문하지 않았다면
                visited[adj] = True # 방문 처리
                stack.append(adj) # 스택에 넣기
                
dfs(1)
print(sum(visited) - 1)