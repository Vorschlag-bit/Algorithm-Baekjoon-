from sys import stdin as input
from collections import defaultdict
import heapq

n,e = map(int,input.readline().split())
graph = defaultdict(list)
m = float('inf')
for _ in range(e):
    a,b,c = map(int,input.readline().split())
    m = min(m,c)
    graph[a].append((b,c))
    graph[b].append((a,c))

# 최소 스패닝 트리 = 주어진 모든 정점들을 연결하는 부분 그래프 중에서 가중치 합이 최소인 트리
# 힙을 사용해서 최소 신장 트리 구하면 되는데, 시작점을 어떻게 할 것인가
# 시작점 안 중요, 어차피 다 들릴 것.
# 특정 노드가 MST에 포함됐는지 안 됐는지 확인
visit = [False] * (n + 1)
ans = 0
q = []
# t,cur
heapq.heappush(q,(0,1))
while q:
    t,cur = heapq.heappop(q)
    if visit[cur]: continue
    visit[cur] = True
    ans += t
    for nxt,cost in graph[cur]:
        if not visit[nxt]:
            heapq.heappush(q,(cost,nxt))

print(ans)