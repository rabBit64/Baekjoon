import sys
INF = sys.maxsize
def solution(n, s, a, b, fares):
    answer = 0
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j]=0
    for e1,e2,v in fares:
        graph[e1][e2]=v
        graph[e2][e1]=v
    #print(graph)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    min_cost=INF
    for i in range(1,n+1):
        min_cost = min(min_cost,min(graph[s][a]+graph[s][b],graph[s][i]+graph[i][a]+graph[i][b]))
    answer=min_cost
    #print(min_cost)
    return answer