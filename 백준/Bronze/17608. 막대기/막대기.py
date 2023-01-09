import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
  num = int(sys.stdin.readline())
  if len(stack)>0:
    if stack[-1]<=num:
      #큰 경우엔 자신보다 클때까지 뺀다
      while True:
        if len(stack)==0 or stack[-1]>num: 
          break
        stack.pop()
      stack.append(num)
    else:
      stack.append(num)
  else:
    stack.append(num)
print(len(stack))