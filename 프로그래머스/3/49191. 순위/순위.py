from collections import defaultdict,deque
def solution(n, results):
    ans = 0
    # a,b -> a가 b를 이김
    p_graph = defaultdict(list)
    c_graph = defaultdict(list)
    for a,b in results:
        p_graph[b].append(a)
        c_graph[a].append(b)
    def p_bfs(i):
        q = deque()
        visit = [False]*(n+1)
        visit[i] = True
        q.append(i)
        cnt = 0
        while q:
            cur = q.popleft()
            for nxt in p_graph[cur]:
                if not visit[nxt]:
                    visit[nxt] = True
                    q.append(nxt)
                    cnt += 1
        return cnt
    def c_bfs(i):
        q = deque()
        visit = [False]*(n+1)
        visit[i] = True
        q.append(i)
        cnt = 0
        while q:
            cur = q.popleft()
            for nxt in c_graph[cur]:
                if not visit[nxt]:
                    visit[nxt] = True
                    q.append(nxt)
                    cnt += 1
        return cnt
    for i in range(1,n+1):
        # 부모와 자식 합
        cnt = 1
        cnt += p_bfs(i)
        cnt += c_bfs(i)
        if cnt == n: ans += 1
    return ans