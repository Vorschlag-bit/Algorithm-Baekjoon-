from collections import deque
from sys import stdin as input

m, n, k = map(int, input.readline().split())
ans = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

arr = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y, X, Y = map(int, input.readline().split())
    # 모눈종이 채우기
    for i in range(x, X):
        for j in range(y, Y):
            arr[i][j] += 1

def check(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    size = 1
    q = deque()
    arr[x][y] += 1
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if check(nx ,ny) and arr[nx][ny] == 0:
                arr[nx][ny] += 1
                q.append((nx, ny))
                size += 1
    return size

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            size = bfs(i, j)
            ans.append(size)

ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))