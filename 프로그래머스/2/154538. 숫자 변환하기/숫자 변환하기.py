from collections import deque
def solution(x, y, n):
    # x -> y는 증가하는 방향 뿐
    q = deque()
    visit = [False] * (y+1)
    visit[x] = True
    q.append((x,0))
    while q:
        cur,cnt = q.popleft()
        if cur == y:
            return cnt
        nxt1 = cur + n
        if nxt1 <= y and not visit[nxt1]:
            visit[nxt1] = True
            q.append((nxt1,cnt+1))
        nxt2 = cur * 2
        if nxt2 <= y and not visit[nxt2]:
            visit[nxt2] = True
            q.append((nxt2,cnt+1))
        nxt3 = cur * 3
        if nxt3 <= y and not visit[nxt3]:
            visit[nxt3] = True
            q.append((nxt3,cnt+1))
    return -1