S = input()
alpha = [-1 for _ in range(26)]
for idx,s in enumerate(S):
  if alpha[ord(s)-97]==-1:
    alpha[ord(s)-97]=idx

print(*alpha)
