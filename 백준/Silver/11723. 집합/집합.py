import sys
M = int(input())
S = set()
for _ in range(M):
  tmp = sys.stdin.readline().strip().split()

  if len(tmp)==1:
    if tmp[0]=="all":
      for i in range(1,21):
        S.add(i)
    elif tmp[0]=="empty":
      S.clear()
  else:
    oper,num = tmp[0],int(tmp[1])
    if oper=="add":
      S.add(num)
    elif oper=="remove":
      S.discard(num)
    elif oper=="check":
      if num in S:
        print(1)
      else:
        print(0)
    elif oper=="toggle":
      if num in S:
        S.remove(num)
      else:
        S.add(num)