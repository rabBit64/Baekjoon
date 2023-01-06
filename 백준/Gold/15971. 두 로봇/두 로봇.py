from collections import deque
n,start,end = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
	n1,n2,e = map(int,input().split())
	graph[n1].append((n2,e))
	graph[n2].append((n1,e))

def bfs():
	visited = [False] * (n+1)
	visited[start] = True
	q = deque([(start,0,0)]) #현재노드, 전체길이, 제일긴길이
	while q:
		cur,total,maxlen = q.pop()
		if cur == end:
			print(total-maxlen)
			break
		for nxt,edge in graph[cur]:
			if not visited[nxt]:
				visited[nxt] = True
				q.appendleft((nxt,total+edge,max(maxlen,edge)))
bfs()
