str = input()
#세개로 쪼개기. 길이 1이상
ans = []
for i in range(len(str)-1):
  for j in range(i+1,len(str)-1):
    tmp = ''
    a = str[:i+1]
    b = str[i+1:j+1]
    c = str[j+1:]
    tmp+=a[::-1]+b[::-1]+c[::-1]
    ans.append(tmp)
ans.sort()
print(ans[0])