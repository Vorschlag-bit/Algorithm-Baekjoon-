from collections import defaultdict,deque
def solution(n, wires):
    ans = float('inf')
    graph = defaultdict(list)
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    def bfs(s):
        nonlocal ans
        q = deque()
        visit = [False]*(n+1)
        visit[s] = True
        cnt = 1
        q.append(s)
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                if not visit[nxt]:
                    visit[nxt] = True
                    q.append(nxt)
                    cnt += 1
        a = abs(abs(n - cnt)-cnt)
        ans = min(ans,a)
    for v1,v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        bfs(1)
        graph[v1].append(v2)
        graph[v2].append(v1)
    return ans