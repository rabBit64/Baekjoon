'''
일단 dfs로 풀면 시간초과 떳다
플로이드 와샬이라고 하는구만: 모든 지점에서 모든 지점까지 최단경로를 모두 구하는것'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
# 그래프 만들때 2차원 리스트 만들고 무한대로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신에서 자기자신으로는 0으로 초기화
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  s,e,w = map(int,input().split())
  if w<graph[s][e]:
    graph[s][e]=w
#print(graph)
#print(graph)
#플로이드 와샬 알고리즘
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      #print("a",a,"b",b,"graph[a][b]",graph[a][b],"graph[a][k]+graph[k][b]",graph[a][k]+graph[k][b])
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b]==INF:
      print(0,end=' ')
    else:
      print(graph[a][b],end=' ')
  print()