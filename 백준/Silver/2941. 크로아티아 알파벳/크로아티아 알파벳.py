'''
내풀이
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
S = input()
cnt = 0
i=0
while i<len(S):
  if S[i:i+2] in alpha:
    cnt+=1
    i+=2
  elif S[i:i+3] in alpha:
    cnt+=1
    i+=3
  else:
    cnt+=1
    i+=1
print(cnt)
'''
word = input()
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lst:
    word = word.replace(i,'*')
print(len(word))