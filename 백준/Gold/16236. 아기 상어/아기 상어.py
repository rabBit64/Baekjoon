'''
시간초과 떳음
찾아보니 상어크기가 9이상 되는 경우 무한루프 ->무한루프는 해결. 틀림
틀린반례
3
0 1 1
4 4 4
1 9 0
0 (정답:1) 
못먹는경우 처리 제대로(크기 작아도 도달할 수 없는 경우 )'''
from collections import deque
import sys
#입력
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
  arr.append(list(map(int,input().split())))
shark_y=0
shark_x=0
for i in range(N):
  for j in range(N):
    if arr[i][j]==9:
      shark_y=i
      shark_x=j

#최단거리
dir = ((1,0),(0,1),(-1,0),(0,-1))
def bfs(fish_y,fish_x):
  visited = [[False]*(N+1) for _ in range(N+1)]
  q = deque()
  q.append((shark_y,shark_x,0))
  visited[shark_y][shark_x]=True
  dist=0
  while q:
    cur_y,cur_x,cur_dist=q.popleft()
    if cur_y==fish_y and cur_x==fish_x:
      #print("return dist",cur_dist)
      return cur_dist
    for i in range(4):
      ny = cur_y+dir[i][0]
      nx = cur_x+dir[i][1]
      if 0<=ny<N and 0<=nx<N:
        if not visited[ny][nx] and arr[ny][nx]<=shark_size and arr[ny][nx]!=9:
          q.append((ny,nx,cur_dist+1))
          visited[ny][nx]=True
  return False #못먹음


shark_size=2
shark_eat=0
ans=0

while True:
  edible=[]
  #1.먹을 수 있는 물고기 구하기
  for i in range(N):
    for j in range(N):
      if arr[i][j]==0:
        continue
      if arr[i][j]<shark_size:
        edible.append([i,j])
  #잡아먹기
  min_dist=1e8
  go_for_eat=[]
  cant_eat=False
  #print("edible before",edible)
  remove_list=[]
  for idx in range(len(edible)):
    fish_y,fish_x=edible[idx]
    dist = bfs(fish_y,fish_x)
    #print("y",fish_y,"x",fish_x,"dist",dist)
    if dist==False:
      #edible.remove([fish_y,fish_x]) #일단 못먹는 물고기는 제거하고 시작! (추가) (앗 중간에 제거하면 문제생김. 반복문 돌때)
      remove_list.append([fish_y,fish_x])
      #print("removed",edible)
    elif dist<min_dist: #딱 한마리만
      min_dist=dist
      go_for_eat.clear()
      go_for_eat.append([fish_y,fish_x])
  for e in remove_list:
    #print(e)
    edible.remove(e)
   #먹을 수 있는 물고기 없으면 끝내기
  #print("edible removed",edible)
  if len(edible)==0:
    print(ans)
    break

  ans+=min_dist
  #print("min_dist",min_dist,"ans",ans)
  #print(go_for_eat)
  #print("현상어위치",shark_y,shark_x)
  arr[shark_y][shark_x]=0 #상어이동
  shark_eat+=1 #먹기
  shark_y=go_for_eat[0][0]
  shark_x=go_for_eat[0][1]
  arr[shark_y][shark_x]=9
  #print(arr)
  #print("shark size",shark_size)
  #상어크기조정
  if shark_eat==shark_size:
    shark_eat=0
    shark_size+=1
  #먹을수있는 물고기 초기화
  edible.clear()
