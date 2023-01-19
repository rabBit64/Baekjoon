S = input()
left = 0
right = 0
for i in range(S.find('(')):
  if S[i]=='@':
    left+=1
for j in range(S.find(')'),len(S)):
  if S[j]=='@':
    right+=1
print(left,right)