def calendar(M,N,x,y):
  while x<=M*N:
    if (x-y)%N==0:
      return x
    x+=M
  return -1

T = int(input())
for _ in range(T):
  M,N,x,y = map(int,input().split())
  print(calendar(M,N,x,y))

