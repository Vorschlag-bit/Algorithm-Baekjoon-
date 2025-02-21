from collections import deque
def solution(k, d):
    ans = 0
    q = deque()
    n = len(d)
    visit = [False] * n
    q.append((k, 0, visit))
    while q:
        st, cnt, visit = q.popleft()
        if cnt > ans:
            ans = cnt
        for i in range(n):
            if not visit[i] and st >= d[i][0]:
                eachv = visit[:]
                eachv[i] = True
                q.append((st - d[i][1], cnt + 1, eachv))
    return ans