from collections import deque, defaultdict
from sys import stdin as input

n, q = map(int, input.readline().split())
graph = defaultdict(list)

for _ in range(n-1):
    a,b,d = map(int, input.readline().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

for _ in range(q):
    k,v = map(int,input.readline().split())
    q = deque()
    visit = [False] * (n+1)
    visit[v] = True
    q.append(v)
    cnt = 0
    while q:
        cur = q.popleft()
        for nxt,dis in graph[cur]:
            if not visit[nxt] and dis >= k:
                cnt += 1
                visit[nxt] = True
                q.append(nxt)
    print(cnt)