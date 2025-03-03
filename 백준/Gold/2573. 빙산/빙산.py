from collections import deque
from sys import stdin as input

n, m = map(int, input.readline().split())
ans = 0
# 빙산 배열
arr = [list(map(int, input.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q = deque()
    visit[x][y] += 1
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        sea = 0
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not check(nx, ny): continue
            # cx, cy에 닿은 바다 개수
            if arr[nx][ny] <= 0:
                sea += 1
            if visit[nx][ny] == 0 and arr[nx][ny] > 0:
                visit[nx][ny] += 1
                q.append((nx, ny))
        ocean.append((cx, cy, sea))

flag = False
while not flag:
    cnt = 0
    ocean = []
    # 빙산 카운트
    visit = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and visit[i][j] == 0:
                bfs(i, j)
                cnt += 1
    # 빙산이 한 덩이도 안 나오면 melt
    if cnt == 0:
        flag = True
    if cnt >= 2:
        break
    # 녹이기
    for s in ocean:
        a = s[0]
        b = s[1]
        c = s[2]
        arr[a][b] -= c
    # 녹을 때마다 해 증가
    ans += 1

print(ans if not flag else 0)
