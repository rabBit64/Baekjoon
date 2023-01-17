N = int(input())
#1,5,10,50
#조합....


sel = []

num = [1,5,10,50]
s = set()
def select(cur):
  sum = 0
  if len(sel)==N:
    for i in sel:
      sum+=i
    if sum not in s:
      s.add(sum)
    return
  for i in range(cur,4):
    sel.append(num[i])
    select(i)
    sel.pop()
select(0)
print(len(s))