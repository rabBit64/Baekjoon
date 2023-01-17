'''
일단 접근방식을 모르겠음..
'''
from collections import deque
N,M =map(int,input().split())
arr = [list(input().strip()) for _ in range(N)]

dir = ((1,0),(0,1),(-1,0),(0,-1))
def bfs():
  while coin:
    by1,bx1,by2,bx2,cnt = coin.popleft()
    if cnt>=10:
      return -1

    for k in range(4):
      ny1=by1+dir[k][0]
      nx1=bx1+dir[k][1]
      ny2=by2+dir[k][0]
      nx2=bx2+dir[k][1]

      if 0 <= nx1 < M and 0 <= ny1 < N and 0 <= nx2 < M and 0 <= ny2 < N:
        if arr[ny1][nx1]=='#':
          ny1=by1
          nx1=bx1
        if arr[ny2][nx2]=='#':
          ny2=by2
          nx2=bx2
        coin.append((ny1,nx1,ny2,nx2,cnt+1))
      elif 0<=ny1<N and 0<=nx1<M:
        return cnt+1
      elif 0<=ny2<N and 0<=nx2<M: 
        return cnt+1
      else:
        continue
  return -1

      
ball = []
for i in range(N):
  for j in range(M):
    if arr[i][j]=='o':
      ball.append((i,j))
coin = deque()
coin.append((ball[0][0],ball[0][1],ball[1][0],ball[1][1],0))
print(bfs())