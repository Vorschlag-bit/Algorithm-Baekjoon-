import heapq
from collections import defaultdict
def solution(n, costs):
    q = []
    cost = [float('inf')]*n
    graph = defaultdict(list)
    for a,b,c in costs:
        graph[a].append((b,c))
        graph[b].append((a,c))
    heapq.heappush(q,(0,0))
    visit = [False]*n
    cost[0] = 0
    ans = 0
    while q:
        co,cur = heapq.heappop(q)
        if visit[cur]: continue
        visit[cur] = True
        ans += co
        for nxt,c in graph[cur]:
            if not visit[nxt] and cost[nxt] > c:
                cost[nxt] = c
                heapq.heappush(q,(c,nxt))
    return ans