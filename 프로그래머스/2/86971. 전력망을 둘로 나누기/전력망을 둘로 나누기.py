from collections import deque
def solution(n, wires):
    ans = len(wires)
    
    def bfs(c):
        q = deque()
        graph = [[] for _ in range(n+1)]
        for idx,(n1,n2) in enumerate(wires):
            if idx == c: continue
            graph[n1].append(n2)
            graph[n2].append(n1)
        visit = [False] * (n+1)
        visit[1] = True
        q.append(1)
        cnt = 1
        
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if not visit[nxt]:
                    cnt += 1
                    visit[nxt] = True
                    q.append(nxt)
        return abs(cnt - abs(n-cnt))
    
    for i in range(len(wires)):
        d = bfs(i)
        ans = min(ans,d)
    return ans