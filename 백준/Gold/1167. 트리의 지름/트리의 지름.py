'''
정답 본 풀이법..
첫번째 노드에서 제일 먼 노드 찾기.
다시 dfs 돌리기
일단 visited에 거리 기록하는 아이디어..'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
  arr = list(map(int,input().split()))
  for i in range(1,len(arr)-1,2):
    graph[arr[0]].append([arr[i],arr[i+1]])
#print(graph)

visited = [-1] * (V+1)
def dfs(start,dist): 
  for b,w in graph[start]:
    if visited[b]==-1:
      visited[b]= w+dist #이부분.탐색하기까지 걸린 간선거리로 초기화
      dfs(b,w+dist)

visited[1]=0
dfs(1,0) #첫번째 노드 시작
#print(max(visited))
start = visited.index(max(visited)) #요 트릭
visited = [-1] * (V+1)
visited[start]=0
dfs(start,0)
print(max(visited))