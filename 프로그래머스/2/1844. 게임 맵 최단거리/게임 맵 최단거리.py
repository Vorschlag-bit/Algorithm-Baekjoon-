from collections import deque
def solution(maps):
    ans = -1
    m = len(maps[0])
    n = len(maps)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit = [[False] * m for _ in range(n)]
    def check(x, y):
        return 0 <= x < n and 0 <= y < m
    q = deque()
    q.append((0, 0, 1))
    visit[0][0] = True
    while q:
        x, y, step = q.popleft()
        if x == n - 1 and y == m - 1:
            ans = step
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not check(nx, ny): continue
            if not visit[nx][ny] and maps[nx][ny] == 1:
                visit[nx][ny] = True
                q.append((nx, ny, step + 1))
    return ans
