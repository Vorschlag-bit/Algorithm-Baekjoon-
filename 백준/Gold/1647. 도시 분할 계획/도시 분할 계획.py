from sys import stdin as input
from collections import defaultdict
import heapq

# n은 10만, m은 100만
# 집,길
n,m = map(int,input.readline().split())

graph = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

m = 0
visit = [False] * (n+1)
q = []
ans = 0
heapq.heappush(q,(0,1))
while q:
    cost,cur = heapq.heappop(q)
    if visit[cur]: continue
    visit[cur] = True
    ans += cost
    m = max(m,cost)
    for nxt,co in graph[cur]:
        if not visit[nxt]:
            heapq.heappush(q,(co,nxt))
print(ans - m)