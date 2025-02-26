from collections import deque
from sys import stdin as input

n = int(input.readline().rstrip())

arr = []

for i in range(n):
    row = list(map(int, input.readline().rstrip()))
    arr.append(row)

ans = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    return 0<= x < n and 0<= y < n

def bfs(i, j):
    q = deque()
    arr[i][j] += 1
    size = 1
    q.append((i, j))
    while q:
        cx, cy = q.popleft()
        for a in range(4):
            nx = cx + dx[a]
            ny = cy + dy[a]
            if check(nx, ny) and arr[nx][ny] == 1:
                arr[nx][ny] += 1
                size += 1
                q.append((nx, ny))
    return size
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            size = bfs(i, j)
            ans.append(size)
ans.sort()
print(len(ans))
for i in ans:
    print(i)