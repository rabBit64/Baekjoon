N,M,V = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
visited2 = [False]*(N+1)
def dfs(cur):
  visited2[cur] = True
  print(cur,end=' ')

  for i in range(1,N+1):
    if not visited2[i] and graph[cur][i]:
      visited2[i]=True
      dfs(i)

def bfs():
  q = [V] #파이썬에선 리스트를 그냥 큐처럼 쓰자..
  visited[V] = True

  while q:
    cur = q.pop(0)
    print(cur, end=' ')
    for i in range(1,N+1):
      if not visited[i] and graph[cur][i]:
        visited[i]= True
        q.append(i)

for _ in range(M):
  a,b = map(int,input().split())
  graph[a][b] = graph[b][a]=1

dfs(V)
print()
bfs()
