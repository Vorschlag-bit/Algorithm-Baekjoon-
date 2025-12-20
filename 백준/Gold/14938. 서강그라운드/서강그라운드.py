from sys import stdin as input
from collections import defaultdict
import heapq

n,m,r = map(int,input.readline().split())
# 1-based
cost = [0] + list(map(int,input.readline().split()))
graph = defaultdict(list)

for _ in range(r):
    a,b,l = map(int,input.readline().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

# 어느 노드에 최소 비용으로 노달하면 최대한 먼 거리를 도달 => 최대 개수 보장
# 모든 지점을 시작점으로 했을 때 최댓값
ans = 0

def dijkstra(start):
    global ans,cost,graph,n,m
    visit = [float('inf')] * (n+1)
    q = []
    heapq.heappush(q,(start,0))
    visit[start] = 0
    while q:
        cur,til = heapq.heappop(q)
        if til > visit[cur]: continue

        for nxt,c in graph[cur]:
            total = til + c
            if total > m: continue
            if visit[nxt] >= total:
                visit[nxt] = total
                heapq.heappush(q,(nxt,total))

    # 방문 가능한 모든 노드 방문 후, 최댓값 계산
    cnt = 0
    for node in range(1,n+1):
        if visit[node] != float('inf'):
            cnt += cost[node]
    ans = max(ans,cnt)

for node in range(1,n+1):
    dijkstra(node)

print(ans)