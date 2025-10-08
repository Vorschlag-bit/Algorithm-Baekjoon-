import heapq
from collections import defaultdict
def get_d(dis,s,graph):
    dis[s] = 0
    q = []
    heapq.heappush(q,(s,0))
    while q:
        cur,cd = heapq.heappop(q)
        if dis[cur] < cd: continue
        for nxt,cost in graph[cur]:
            if dis[nxt] <= cost + cd: continue
            dis[nxt] = cost + cd
            heapq.heappush(q,(nxt,cost+cd))

def get_cost(t,s,graph,n):
    dis = [float('inf')] * (n+1)
    dis[s] = 0
    q = []
    heapq.heappush(q,(s,0))
    while q:
        cur,cd = heapq.heappop(q)
        if dis[cur] < cd: continue
        for nxt,cost in graph[cur]:
            if dis[nxt] <= cd + cost: continue
            dis[nxt] = cost + cd
            heapq.heappush(q,(nxt,cost+cd))        
    return dis[t]
            
def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    # 1. 출발지에서 합승 마지막 지점까지 dijk
    d = [float('inf')] * (n+1)
    get_d(d,s,graph)
    # 각각 최소 가격으로 집 갈 경우
    ans = get_cost(a,s,graph,n) + get_cost(b,s,graph,n)
    # 2. A에서 모든 곳까지
    ad = [float('inf')] * (n+1)
    get_d(ad,a,graph)
    # 3. B에서 모든 곳까지
    bd = [float('inf')] * (n+1)
    get_d(bd,b,graph)
    for i in range(1,n+1):
        if s == i: continue
        # 중간 지점 찾기
        base = d[i]
        # 중간 지점 못 찾으면 pass
        if base == float('inf'): continue
        ta = ad[i]
        tb = bd[i]
        if ta != float('inf') and tb != float('inf'):
            ans = min(ans,tb+ta+base)
    return ans