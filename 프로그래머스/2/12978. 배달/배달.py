from collections import defaultdict
import heapq
def solution(n, road, k):
    ans = 0
    q = []
    dis = [float('inf')]*(n+1)
    dis[0] = 0
    dis[1] = 0
    graph = defaultdict(list)
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    heapq.heappush(q,(0,1))
    while q:
        time,cur = heapq.heappop(q)
        if dis[cur] < time: continue
        for nxt,cost in graph[cur]:
            if dis[nxt] > time + cost:
                dis[nxt] = time + cost
                heapq.heappush(q,(cost+time,nxt))
    for d in range(1,n+1):
        if dis[d] <= k: ans += 1
    return ans