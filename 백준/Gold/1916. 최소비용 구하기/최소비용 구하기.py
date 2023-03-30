import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a,b,e = map(int,input().split())
  graph[a].append([b,e])
start,end = map(int,input().split())
dist = [INF] * (N+1)
def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  dist[start]=0
  while q:
    curdist,curnode = heapq.heappop(q)

    if dist[curnode]<curdist:
      continue
    for i in graph[curnode]:
      nnode,ndist = i[0],i[1]
      #print("nnode",nnode)
      cost = dist[curnode]+ndist
      if cost<dist[nnode]:
        dist[nnode]=cost
        heapq.heappush(q,(cost,nnode))
dijkstra(start)
print(dist[end])

