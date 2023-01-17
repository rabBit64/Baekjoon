'''
1차 시도 일단 시간초과..
arr = [list(map(int,input().strip())) for _ in range(N)]
'''
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(N)] # 일단 이렇게 입력받기..
dir = [(1,0),(0,1),(-1,0),(0,-1)]

def move(i,j):
  cnt=1
  group = []
  visited[i][j]=True
  q = deque()
  q.append((i,j))
  group.append((i,j))
  while q:
    cy,cx = q.popleft()
    for k in range(4):
      ny = cy+dir[k][0]
      nx = cx+dir[k][1]
      if 0<=ny<N and 0<=nx<M:
        if arr[ny][nx]==0 and not visited[ny][nx]:
          visited[ny][nx]=True
          q.append((ny,nx))
          group.append((ny,nx))
          cnt+=1
  return cnt,group
# 1.0의 묶음 구하기.
visited = [[False]*(M) for _ in range(N)]
tmp = [[0]*(M) for _ in range(N)]
tmp_group = [[0]*(M) for _ in range(N)]
group_num=1
for i in range(N):
  for j in range(M):
    if not visited[i][j] and arr[i][j]==0:
      cnt,group=move(i,j)
      for gy,gx in group:
        tmp[gy][gx]=cnt
        tmp_group[gy][gx]=group_num
      group_num+=1
# 원래 빈칸인곳0, 벽은 이동할수있는칸 나누기10
for i in range(N):
  for j in range(M):
    if arr[i][j]==0:
      print(0,end='')
    elif arr[i][j]==1:
      s = set()
      for k in range(4):
        y=i+dir[k][0]
        x=j+dir[k][1]
        if 0<=x<M and 0<=y<N:
          #같은 그룹에 속해있지 않을때만
          if tmp_group[y][x] not in s:
            arr[i][j]+=tmp[y][x]
            s.add(tmp_group[y][x])
      print(arr[i][j]%10,end='')
  print()

'''
이렇게 하면 시간초과남
def move(i,j):
  cnt = 1
  visited = [[False] * (M+1) for _ in range(N+1)]
  q = deque()
  q.append((i,j))
  visited[i][j]=True
  while q:
    cy,cx = q.popleft()
    for k in range(4):
      nx = cx+dir[k][0]
      ny = cy+dir[k][1]
      if 0<=ny<N and 0<=nx<M:
        if arr[ny][nx]==0 and not visited[ny][nx]:
          visited[ny][nx]=True
          q.append((ny,nx))
          cnt+=1
  return cnt
#벽인 경우 이동할 수 있는칸
ans = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
  for j in range(M):
    if arr[i][j]==1:
      cnt = move(i,j)
      print(cnt,end='')
    else:
      print(0,end='')
  print()
'''