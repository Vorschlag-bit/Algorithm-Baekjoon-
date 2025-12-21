from sys import stdin as input
from collections import defaultdict
import heapq

n = int(input.readline())
m = int(input.readline())
graph = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,input.readline().split())
    graph[a].append((b,c))

s,t= map(int,input.readline().split())

route = []
ans = float('inf')
visit = [float('inf')] * (n+1)
visit[s] = 0
q = []
heapq.heappush(q,(0,s))
ex = [float('inf')] * (n+1)
while q:
    til,cur = heapq.heappop(q)
    if visit[cur] < til: continue
    for nxt,cost in graph[cur]:
        total = til + cost
        if total >= visit[nxt]: continue
        visit[nxt] = total
        ex[nxt] = cur
        heapq.heappush(q,(total,nxt))

print(visit[t])

cur = t
route.append(t)
while cur != s:
    route.append(ex[cur])
    cur = ex[cur]

print(len(route))
print(' '.join(map(str,route[::-1])))