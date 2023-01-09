import sys

def DFS(idx, total):
  #print(total)
  global s
  if total>s:
    return
  if idx==k:
    if 0<total<=s:
      ch[total]=True
  else:
    DFS(idx+1,total+arr[idx])
    DFS(idx+1,total-arr[idx])
    DFS(idx+1,total)

input = sys.stdin.readline
k = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
ch = [False]*(s+1)
DFS(0,0)
ans = 0
for b in ch:
  if b==False:
    ans+=1
print(ans-1)