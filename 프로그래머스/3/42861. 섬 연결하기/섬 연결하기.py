import heapq
from collections import defaultdict
def solution(n, costs):
    q = []
    # 그니까;; 0에서 출발했을 때 최솟값이라 생각했는데....
    graph = defaultdict(list)
    for a,b,c in costs:
        graph[a].append((b,c))
        graph[b].append((a,c))
    heapq.heappush(q,(0,0))
    ans = 0
    visit = [False]*n
    while q:
        co,cur = heapq.heappop(q)
        if visit[cur]: continue
        visit[cur] = True
        ans += co
        for nxt,c in graph[cur]:
            if not visit[nxt]:
                heapq.heappush(q,(c,nxt))
    return ans