import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

white = 0
blue = 0
def recursion(y,x,size):
  global white,blue
  cnt = 0
  for i in range(y,y+size):
    for j in range(x,x+size):
      if arr[i][j]:
        cnt+=1
  
  if cnt==0:
    white+=1
  elif cnt==size**2:
    blue+=1
  else:
    recursion(y,x,size//2)
    recursion(y,x+size//2,size//2)
    recursion(y+size//2,x,size//2)
    recursion(y+size//2,x+size//2,size//2)
  return

recursion(0,0,n)
print(white)
print(blue)