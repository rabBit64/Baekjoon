'''
5/1
분할정복

'''
A, B, C = map(int,input().split())

def f(B):
  if(B==1):
    return A%C
  k = f(B//2)%C
  if(B%2==0):
    return k*k%C
  else:
    return k*k%C*A%C
print(f(B))