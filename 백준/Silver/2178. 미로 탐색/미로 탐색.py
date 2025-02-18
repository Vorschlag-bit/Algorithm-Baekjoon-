from sys import stdin as input
from collections import deque

n, m = map(int, input.readline().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = []
for i in range(n):
    row = list(map(int, input.readline().strip()))
    arr.append(row)
visit = [[False] * m for _ in range(n)]

def check(x, y):
    return 0 <= x < n and 0 <= y < m
def bfs(x, y):
    q = deque()
    visit[x][y] = True
    q.append((x, y, 0))
    while q:
        nx, ny, step = q.popleft()
        if nx == n - 1 and ny == m - 1:
            print(step + 1)
            exit()
        for i  in range(4):
            cx = nx + dx[i]
            cy = ny + dy[i]
            if not check(cx, cy): continue
            if not visit[cx][cy] and arr[cx][cy] != 0:
                visit[cx][cy] = True
                q.append((cx, cy, step + 1))
bfs(0, 0)