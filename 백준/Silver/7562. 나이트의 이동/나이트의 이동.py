from collections import deque
from sys import stdin as input

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

t = int(input.readline().rstrip())

def check(x, y, l):
    return 0 <= x < l and 0 <= y < l

def bfs(x, y, tx, ty, l):
    q = deque()
    visit[x][y] = True
    q.append((x, y))
    while q:
        nx, ny = q.popleft()
        if nx == tx and ny == ty:
            return arr[nx][ny]
        for i in range(8):
            cx = nx + dx[i]
            cy = ny + dy[i]
            if check(cx, cy, l) and not visit[cx][cy]:
                visit[cx][cy] = True
                arr[cx][cy] = arr[nx][ny] + 1
                q.append((cx, cy))

for _ in range(t):
    l = int(input.readline().rstrip())
    arr = [[0] * l for _ in range(l)]
    visit = [[False] * l for _ in range(l)]
    i, j = map(int, input.readline().split())
    ti, tj = map(int, input.readline().split())
    print(bfs(i,j ,ti, tj, l))