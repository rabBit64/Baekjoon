from collections import deque
node = int(input())
edge = int(input())
graph = [[] for _ in range(node+1)]
visited = [False for _ in range(node+1)]
def dfs(start):
  visited[start]=True
  q = deque([start])
  cnt=0
  while q:
    cur = q.popleft()
    for i in graph[cur]:
      if not visited[i]:
        q.append(i)
        visited[i]=True
        cnt+=1
  return cnt

for _ in range(edge):
  a,b = map(int,input().split())
  graph[a]+=[b]
  graph[b]+=[a]
ans=dfs(1)
print(ans)