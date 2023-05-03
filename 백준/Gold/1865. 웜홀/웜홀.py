'''
음수 가중치 - 벨만포드
'''
import sys
INF = 1e+8
input = sys.stdin.readline

TC = int(input())
def hole(graph,N,distance):
    distance[1] = 0
    for check in range(N):
        for vertex in range(1,N+1):
            for next_vertex, next_cost in graph[vertex]:
                if distance[next_vertex] > distance[vertex]+next_cost:
                    distance[next_vertex] = distance[vertex]+next_cost
                    if check == N-1:
                        return False
    return True
        
for _ in range(TC):
    N,M,W = map(int,input().split())
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        S,E,T = map(int,input().split())
        graph[S].append([E,T])
        graph[E].append([S,T])
    for _ in range(W):
        WS,WE,WT = map(int,input().split())
        graph[WS].append([WE,-1*WT])
    # print("graph",graph)
    if hole(graph,N,distance):
        print("NO")
    else:
        print("YES")