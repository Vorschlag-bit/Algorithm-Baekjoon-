from collections import deque
def solution(n, wires):
    def bfs(cut):
        visit = [False] * (n + 1)
        arr = [[] for _ in range(n + 1)]
        for i, (v1, v2) in enumerate(wires):
            if cut == i: continue
            arr[v1].append(v2)
            arr[v2].append(v1)
            
        start = 1
        cnt = 1
        q = deque()
        q.append(start)
        visit[start] = True
        
        while q:
            cur_node = q.popleft()
            for nxt_node in arr[cur_node]:
                if not visit[nxt_node]:
                    visit[nxt_node] = True
                    q.append(nxt_node)
                    cnt += 1
        return abs(cnt - abs(n - cnt))
    ans = 100
    for i in range(len(wires)):
        diff = bfs(i)
        ans = min(ans, diff)
    return ans