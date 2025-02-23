from collections import deque
from sys import stdin as input

m, n, h = map(int, input.readline().split())
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

arr = []
q = deque()
for height in range(h):
    arrH = []
    for i in range(n):
        arrI = list(map(int, input.readline().split()))
        arrH.append(arrI)
    arr.append(arrH)

def check(z, x, y):
    return 0 <= z < h and 0 <= x < n and 0 <= y < m

ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

while q:
        cz, cx, cy = q.popleft()
        if arr[cz][cx][cy] - 1 > ans:
            ans = arr[cz][cx][cy] - 1
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]
            if check(nz, nx, ny) and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[cz][cx][cy] + 1
                q.append((nz, nx, ny))

flag = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                flag = False
                break
print(ans if flag else -1)

