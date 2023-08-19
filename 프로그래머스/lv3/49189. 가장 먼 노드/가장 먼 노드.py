'''
'''
def bfs(adj,n):
    queue=[1]
    distance = [0 for _ in range(n+1)]
   
    while queue:
        cur = queue.pop(0)
        for next in adj[cur]:
            if distance[next]==0:
                distance[next] = distance[cur]+1
                queue.append(next)        
    print(distance)
    return distance[2:].count(max(distance))
def solution(n, edge):
    answer = 0
    '''
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        graph[edge[i][0]][edge[i][1]]=1
    '''
    adj = [[] for _ in range(n+1)]
    for v1, v2 in edge:
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    answer = bfs(adj,n)
    return answer