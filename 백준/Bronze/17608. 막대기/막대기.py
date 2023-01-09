import sys
def sol():
  input = sys.stdin.readline
  N = int(input())
  arr = [int(input()) for i in range(N)]
  M = 0
  ans = 0
  for num in reversed(arr):
    if num>M:
      M=num
      ans+=1
  return ans
print(sol())