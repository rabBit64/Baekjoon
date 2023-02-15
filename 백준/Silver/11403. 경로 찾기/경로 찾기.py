from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)] #이렇게 한줄로 입력받기!
visited = [[0]*(N) for _ in range(N)]

def bfs(x):
  Q = deque()
  Q.append(x)
  check = [False for _ in range(N)]
  while Q:
    cur = Q.popleft()
    for i in range(N):
      if not check[i] and graph[cur][i]==1:
        check[i]=True
        Q.append(i)
        visited[x][i]=1
for i in range(N):
  bfs(i)
for i in visited:
  print(*i)