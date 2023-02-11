import copy
from collections import deque
N = int(input())
arr=[]
for _ in range(N):
  arr.append(input())
#arr2 = arr #이렇게 바꿀경우 같은 주소!
arr2 = copy.deepcopy(arr) 
for i in range(N):
  arr2[i]=arr2[i].replace('R','G')
visited = [[False]*(N+1) for _ in range(N+1)]
visited2 = [[False]*(N+1) for _ in range(N+1)]
dir=((1,0),(0,1),(-1,0),(0,-1))
def bfs(y,x,matrix,blind):
  if not blind:
    q = deque()
    q.append((y,x))
    cur=matrix[y][x]
    visited[y][x]=True
    while q:
      y,x=q.popleft()
      for i in range(4):
        ny=y+dir[i][0]
        nx=x+dir[i][1]
        if ny>=N or ny<0 or nx>=N or nx<0:
          continue
        if not visited[ny][nx] and matrix[ny][nx]==cur:
          visited[ny][nx]=True
          q.append((ny,nx))
  else:
    q = deque()
    q.append((y,x))
    cur=matrix[y][x]
    visited2[y][x]=True
    while q:
      y,x=q.popleft()
      
      for i in range(4):
        ny=y+dir[i][0]
        nx=x+dir[i][1]
        if ny>=N or ny<0 or nx>=N or nx<0:
          continue
        if not visited2[ny][nx] and matrix[ny][nx]==cur:
          visited2[ny][nx]=True
          q.append((ny,nx))
cnt=0
cnt2=0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      cnt+=1
      bfs(i,j,arr,False)
for i in range(N):
  for j in range(N):
    if not visited2[i][j]:
      cnt2+=1
      bfs(i,j,arr2,True)   
print(cnt,cnt2)