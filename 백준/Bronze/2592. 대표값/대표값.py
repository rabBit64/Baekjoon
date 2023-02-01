arr = [int(input()) for _ in range(10)]
idx = list(arr.count(i) for i in arr)
print(sum(arr)//10)
print(arr[idx.index(max(idx))])
'''
arr = [int(input()) for _ in range(10)]
cnt = {}
for a in arr:
  if a in cnt:
    cnt[a]+=1
  else:
    cnt[a]=1
maxn = 0
ans = 0
for key in cnt:
  if cnt[key]>maxn:
    maxn=cnt[key]
    ans = key
print(int(sum(arr)/10))
print(ans)
'''