T = int(input())
for _ in range(T):
  M,N,x,y = map(int,input().split())

  valid = False
  while x<=M*N:
    if (x-y)%N==0:
      valid = True
      break
    x+=M
  if valid:
    print(x)
  else:
    print(-1)