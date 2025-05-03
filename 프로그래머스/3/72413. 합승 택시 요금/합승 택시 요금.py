from collections import defaultdict
import heapq
def dijkstra(s,dest,visit,graph):
    q = []
    visit[s] = 0
    heapq.heappush(q,(0,s))
    while q:
        cost, cur = heapq.heappop(q)
        if cur == dest:
            return cost
        if visit[cur] < cost:
            continue
        for nxt,c in graph[cur]:
            if visit[nxt] < cost + c:
                continue
            visit[nxt] = cost + c
            heapq.heappush(q,(cost + c,nxt))
    return 0
    
def solution(n, s, a, b, fares):
    ans = float('inf')
    # fares = [c,d,f] c->d f비용
    # a만의 최소 비용 노드 [] + 비용
    # b만의 최소 비용 노드 [] + 비용
    graph = defaultdict(list)
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    visit = [float('inf')]*(n+1)
    # a,b 합승하지 않을 떄의 가격
    acost = dijkstra(s,a,visit,graph)
    bcost = dijkstra(s,b,visit,graph)
    ans = min(ans, acost+bcost)
    # 둘이 갈라지는 지점 정하고 지점에서부터 a,b 각각 가는 걸 생각
    for k in range(1,n+1):
        if k == s: continue
        # 갈라지는 지점까지의 비용
        cost = visit[k]
        avisit = [float('inf')] * (n+1)
        bvisit = [float('inf')] * (n+1)
        cost += dijkstra(k,a,avisit,graph)
        cost += dijkstra(k,b,bvisit,graph)
        ans = min(ans, cost)
    return ans