'''
최단시간 bfs
화면에 있는 이모티콘 s개 / 클립보드에 있는 이모티콘 c개
1. 화면에 있는 이모티콘 모두 복사
복사 (s,c) -> (s,s)
2. 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
붙여넣기 (s,s) -> (s+c,c)
3. 화면에 있는 이모티콘 중 하나 삭제
(s,s) -> (s-1,c)
'''
from collections import deque
n = int(input())
dist = [[-1]*(n+1) for _ in range(n+1)]
q = deque()
q.append((1,0)) # 화면 이모티콘, 클립보드 이모티콘
dist[1][0] = 0
while q:
  s,c = q.popleft()
  if dist[s][s] == -1: #방문하지 않음
    dist[s][s] = dist[s][c] + 1
    q.append((s,s))
  if s+c <= n and dist[s+c][c] == -1:
    dist[s+c][c] = dist[s][c] + 1
    q.append((s+c,c))
  if s-1 >= 0 and dist[s-1][c] == -1:
    dist[s-1][c] = dist[s][c] + 1
    q.append((s-1,c))
answer = -1
for i in range(n+1):
  if dist[n][i] != -1:
    if answer == -1 or answer > dist[n][i]:
      answer = dist[n][i]
print(answer)