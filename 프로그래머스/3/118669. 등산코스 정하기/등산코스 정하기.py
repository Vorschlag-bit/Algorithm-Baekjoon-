import heapq
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for i,j,w in paths:
        graph[i].append([j,w])
        graph[j].append([i,w])
        
    summit = [False] * (n+1)
    for s in summits:
        summit[s] = True
    
    dis = [float('inf')] * (n+1)
    pq = []
    # 각 정점을 도달할 수 있는 최소 intensity를 저장할 dis
    for g in gates:
        dis[g] = 0
        heapq.heappush(pq, [0,g])
    
    while pq:
        d, node = heapq.heappop(pq)
        
        if dis[node] < d or summit[node]: continue
        
        for nxt_node,step in graph[node]:
            # w와 현재 노드의 기존 intensity 비교(언제나 dis에는 intensity만 저장)
            step = max(step, dis[node])
            if step < dis[nxt_node]:
                dis[nxt_node] = step
                heapq.heappush(pq, [step,nxt_node])
            
            
    answer = [0,float('inf')]
    for s in sorted(summits):
        if dis[s] < answer[1]:
            answer[0] = s
            answer[1] = dis[s]
    return answer