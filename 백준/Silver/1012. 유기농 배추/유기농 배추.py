from sys import stdin as input
from collections import deque

t = int(input.readline().strip())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y, n, m, arr):
    q = deque()
    arr[x][y] += 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if check(nx, ny, n, m) and arr[nx][ny] == 1:
                arr[nx][ny] += 1
                q.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, input.readline().split())
    arr = [[0] * m for _ in range(n)]
    ans = 0
    # 양배추 위치 초기화
    for c in range(k):
        j, i = map(int, input.readline().split())
        arr[i][j] = 1
    # bfs
    for i in range(n):
        for j in range(m):
            # 방문 처리를 + 1로
            if arr[i][j] == 1:
                bfs(i, j, n, m, arr)
                ans += 1
    print(ans)