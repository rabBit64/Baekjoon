'''
일단 다익스트라 문제였다.. 최소힙을 사용해야 한다는데'''
import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline
V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
  u,v,w = map(int,input().split())
  graph[u].append([v,w])

dist = [INF] * (V+1)
def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  dist[start]=0

  while q:
    cdist,cur = heapq.heappop(q)
    if dist[cur]<cdist:
      continue
    for j in graph[cur]:
      cost = dist[cur]+j[1]
      if cost<dist[j[0]]:
        dist[j[0]]=cost
        heapq.heappush(q,(cost,j[0]))
dijkstra(start)
for i in range(1,V+1):
  if dist[i]==INF:
    print("INF")
  else:
    print(dist[i])
