from sys import stdin as input
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(i, j):
    global maxW
    q = deque()
    visit[i][j] = True
    q.append((i, j))
    width = 1
    
    while q:
        nx, ny = q.popleft()
        for d in range(4):
            x = nx + dx[d]
            y = ny + dy[d]
            if not check(x, y):
                continue

            if arr[x][y] == 1 and not visit[x][y]:
                visit[x][y] = True
                width += 1
                q.append((x, y))
    
    maxW = max(maxW, width)

n, m = map(int, input.readline().split())
arr = []

for _ in range(n):
    i = list(map(int, input.readline().split()))
    arr.append(i)

visit = [[False] * m for _ in range(n)]

maxW = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if not visit[i][j] and arr[i][j] == 1:
            cnt += 1
            bfs(i, j)

print(cnt)
print(maxW)