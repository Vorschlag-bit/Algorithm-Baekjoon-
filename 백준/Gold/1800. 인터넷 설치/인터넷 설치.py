import heapq
from collections import defaultdict
from sys import stdin
input = stdin.readline

n, p, k = map(int, input().split())
graph = defaultdict(list)
for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = -1

def dijkstra(mid):
    q = [(0,1)]
    dis = [float('inf')] * (n+1)
    dis[1] = 0

    while q:
        cnt,node = heapq.heappop(q)
        if dis[node] < cnt: continue
        for nxt,cost in graph[node]:
            c = cnt
            if cost > mid: c += 1
            if c < dis[nxt]:
                dis[nxt] = c
                heapq.heappush(q,(c,nxt))
    return k >= dis[n]

l = 0
r = 1000000
while l < r:
    m = (l+r) // 2
    if dijkstra(m):
        ans = m
        r = m
    else:
        l = m + 1

print(ans)