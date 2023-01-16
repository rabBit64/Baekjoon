'''
놓친거. 일단 visited를 빼먹음
이동하는거. 더하고 빼는게 아니라 업데이트..
'''
from collections import deque
N,M = map(int,input().split())
arr = [-1 for i in range(101)] #0:사다리 1:뱀
ladder = [0 for i in range(101)]
snake = [0 for i in range(101)]
for _ in range(N):
  x,y = map(int,input().split())
  ladder[x] = y
  arr[x] = 0
for _ in range(M):
  u,v = map(int,input().split())
  snake[u] = v
  arr[u] = 1

#1번칸 시작. 100번칸 최소 몇번?
dist = [[0] for _ in range(101)]
visited = [False for _ in range(101)]
dist[1] = 0
q = deque()
q.append((1,0))
visited[1] = True
while q:
  cur,cnt = q.popleft() #현재위치
  if cur==100:
    print(cnt)
    break

  for dice in range(1,7):
    nxt = cur+dice
    if 0<nxt<=100 and visited[nxt]==False:
      if arr[nxt]==0:
        nxt=ladder[nxt]
      elif arr[nxt]==1:
        nxt=snake[nxt]
      if 0<nxt<=100:
        q.append((nxt,cnt+1))
        visited[nxt] = True

