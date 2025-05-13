from collections import defaultdict
from collections import deque
def solution(n, roads, sources, d):
    ans = []
    # 노드 간의 비용 고정 => bfs
    graph = defaultdict(list)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    dis = [-1] * (n+1)
    dis[d] = 0
    visit = [False]*(n+1)
    visit[d] = True
    q = deque()
    q.append((d,0))
    while q:
        cur,time = q.popleft()
        for nxt in graph[cur]:
            if not visit[nxt]:
                visit[nxt] = True
                dis[nxt] = time + 1
                q.append((nxt,time+1))
    for s in sources:
        ans.append(dis[s])
    return ans