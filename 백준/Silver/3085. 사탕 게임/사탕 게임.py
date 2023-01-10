import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)] # 이렇게 띄어쓰기 없을때 입력받기!

def longest():
  max_cnt = 0
  for i in range(n):
    cnt = 1 #틀린점 - 초기화 위치가 틀렸었음
    for j in range(1,n):
      if arr[i][j] == arr[i][j-1]:
        cnt+=1
      else:
        cnt=1
      if cnt>max_cnt:
        max_cnt=cnt
    cnt = 1
    for j in range(1,n):
      if arr[j][i] == arr[j-1][i]:
        cnt+=1
      else:
        cnt=1
      if cnt>max_cnt:
        max_cnt=cnt
  return max_cnt



dir = [[0,1],[1,0],[-1,0],[0,-1]]
answer = longest() # 틀린점2 - swap 안한것도 한번 체크해봐야함
for row in range(n):
  for col in range(n):
    for k in range(4):
      nrow = row+dir[k][0]
      ncol = col+dir[k][1]
      if nrow>=n or nrow<0 or ncol>=n or ncol<0:
        continue
      if arr[row][col] != arr[nrow][ncol]:
        arr[row][col],arr[nrow][ncol] = arr[nrow][ncol],arr[row][col] # 이렇게 바로 swap이 되는구나..
        answer = max(longest(),answer)
        arr[row][col],arr[nrow][ncol] = arr[nrow][ncol],arr[row][col]
print(answer)