'''
모르겠음
왜 플로이드 와샬이지
풀이법.
플로이드로 자신보다 키 큰 학생들 모두 구하기.
graph[i][j] i번학생키<j번학생키
i번학생과 j번 학생의 관계성 구하기
graph[i][j] graph[j][i]
횟수가 정확히 N-1이면 자신 순서 알수 있음'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
  a,b=map(int,input().split())
  graph[a][b]=1 #a < b

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      if graph[i][k]==1 and graph[k][j]==1:
        graph[i][j]=1 # i<j
#print(graph)
ans=0
for i in range(1,N+1):
  cnt=0
  for j in range(1,N+1):
    cnt+=graph[i][j]+graph[j][i]
 # print("cnt",cnt)
  if cnt==N-1:
    ans+=1
print(ans)