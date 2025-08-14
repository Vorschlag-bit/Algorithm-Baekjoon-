from sys import stdin as input
from collections import deque
# 세로, 가로
n,m = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
ans = 0
directions = [(0,1),(1,0),(0,-1),(-1,0)]

def check(x,y):
    return 0 <= x < n and 0 <= y < m

def get_air(x,y,airs):
    q = deque()
    q.append((x,y))
    airs[x][y] = True
    while q:
        cx,cy = q.popleft()
        for d in directions:
            nx,ny = cx+d[0], cy+d[1]
            if not check(nx,ny): continue
            if arr[nx][ny] == 0 and not airs[nx][ny]:
                airs[nx][ny] = True
                q.append((nx,ny))


def bfs(x,y,melts,visit,airs):
    q = deque()
    visit[x][y] = True
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        air = 0
        for d in directions:
            nx,ny = cx+d[0],cy+d[1]
            if not check(nx,ny): continue
            if airs[nx][ny]: air += 1
            if arr[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx,ny))
        if air >= 2:
            melts.append((cx,cy))

while True:
    # 종료 조건
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1: cnt += 1
    if cnt == 0:
        break
    airs = [[False] * m for _ in range(n)]
    # 공기 구하기(최외각)
    for i in range(n):
        if arr[i][0] == 0 and not airs[i][0]:
            get_air(i,0,airs)
        if arr[i][m-1] == 0 and not airs[i][m-1]:
            get_air(i,m-1,airs)
    for j in range(m):
        if arr[0][j] == 0 and not airs[0][j]:
            get_air(0,j,airs)
        if arr[n-1][j] == 0 and not airs[n-1][j]:
            get_air(n-1,j,airs)
    # 녹일 치즈 정하기
    melt = []
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visit[i][j]:
                bfs(i,j,melt,visit,airs)
    # 치즈 녹이기
    for x,y in melt:
        arr[x][y] = 0
    ans += 1
print(ans)