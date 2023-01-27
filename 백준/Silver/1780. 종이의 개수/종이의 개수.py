'''알게된거
set은 인덱싱이 안된다
전역변수를 지역변수로 호출하려면 함수안에서 global 쓰기'''
import sys
input = sys.stdin.readline
N = int(input())
arr = []

cnt = {-1:0, 0:0, 1:0}
visited = [[False]*N for _ in range(N)]
def divide(y,x,size):
  global a,b,c
  if not visited[y][x]:
    if all(arr[y+i][x+j]==arr[y][x] for i in range(size) for j in range(size)):
      cnt[arr[y][x]]+=1
      visited[y][x]=True
      return
    else:
      divide(y,x,size//3) #0,0
      divide(y,x+size//3,size//3) #0,3
      divide(y+size//3,x,size//3) #3,0
      divide(y,x+2*(size//3),size//3) #0,6
      divide(y+size//3,x+size//3,size//3) #3,3 
      divide(y+size//3,x+2*(size//3),size//3) #3,6
      divide(y+2*(size//3),x+size//3,size//3) #6,3
      divide(y+2*(size//3),x,size//3) #6,0
      divide(y+2*(size//3),x+2*(size//3),size//3) #6,6

for _ in range(N):
  arr.append(list(map(int,input().split())))
divide(0,0,N)
print(cnt[-1])
print(cnt[0])
print(cnt[1])