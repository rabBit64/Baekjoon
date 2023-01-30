N = int(input())
M = int(input())
str = input()
P = 'IOI'
for _ in range(N-1):
  P+='OI'
idx = 0
tmp = str
cnt = 0

while True:
  idx = tmp.find(P)
  if idx==-1:
    break
  else:
    cnt+=1
    tmp = tmp[idx+1:]
print(cnt)
