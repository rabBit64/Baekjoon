import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int,input().split())
parent = [0] * (N+1)
for i in range(N+1):
  parent[i]=i

def find_parent(x):
  if (x==parent[x]):
    return x
  parent[x] = find_parent(parent[x])
  return parent[x]

def do_union(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a==b: # 루트노드 같으면 동일한 집합
    return
  if (a>b):
    parent[a] = b
  elif (a<b):
    parent[b] = a

for _ in range(M):
  oper,a,b = map(int,input().split())
  if oper==0:
    do_union(a,b)
  else:
    if(find_parent(a)==find_parent(b)):
      print("YES\n")
    else:
      print("NO\n")