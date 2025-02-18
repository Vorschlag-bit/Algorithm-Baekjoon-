from sys import stdin as input
from collections import deque

tomato = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
m, n = map(int, input.readline().split())

for _ in range(n):
    i = list(map(int, input.readline().split()))
    tomato.append(i)


def check(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(q):
    while q:
        x, y = q.popleft()
        current = tomato[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not check(nx, ny): continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = current + 1
                q.append((nx, ny))
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))
bfs(q)

flag = True
ans = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            flag = False
            break
        if tomato[i][j] > ans:
            ans = tomato[i][j] - 1
print(ans if flag else -1)