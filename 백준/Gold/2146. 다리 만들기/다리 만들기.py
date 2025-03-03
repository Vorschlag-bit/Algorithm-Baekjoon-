from collections import deque
from sys import stdin as input

n = int(input.readline().rstrip())

no = 1
arr = [list(map(int, input.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x,y):
    return 0 <= x < n and 0 <= y < n

def mark(x,y):
    q = deque()
    arr[x][y] += no
    q.append((x,y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not check(nx, ny): continue
            if arr[nx][ny] == 1:
                arr[nx][ny] += no
                q.append((nx,ny))


# 섬 마킹
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            mark(i,j)
            no += 1

def bridge(x,y,island):
    q = deque()
    visit = [[False] * n for _ in range(n)]
    visit[x][y] = True
    q.append((x,y,0))
    while q:
        cx,cy,bridge = q.popleft()
        if arr[cx][cy] != island and arr[cx][cy] > 0:
            return bridge
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not check(nx,ny): continue
            if not visit[nx][ny] and arr[nx][ny] != island:
                visit[nx][ny] = True
                q.append((nx,ny,bridge+1))
    # 바로 종료할 경우 0
    return 0

ans = n * n

for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            b = bridge(i,j,arr[i][j])
            # 바로 종료하는 경우 제외
            if b != 0 and ans > b:
                ans = b
print(ans - 1)