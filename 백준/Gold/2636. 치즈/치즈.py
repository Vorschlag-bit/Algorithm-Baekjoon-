from sys import stdin as input
from collections import deque

r,c = map(int,input.readline().split())

arr = [list(map(int,input.readline().split())) for _ in range(r)]
directions = [(0,1),(1,0),(-1,0),(0,-1)]
rest = 0
ans = 0

def check(x,y):
    return 0 <= x < r and 0 <= y < c

def get_air(x,y,airs):
    q = deque()
    # 공기이지 방문 배열인 airs
    q.append((x,y))
    airs[x][y] = True
    cnt = 1
    while q:
        cx,cy = q.popleft()
        for d in directions:
            nx,ny = cx+d[0],cy+d[1]
            if not check(nx,ny): continue
            if not airs[nx][ny] and arr[nx][ny] == 0:
                cnt += 1
                airs[nx][ny] = True
                q.append((nx,ny))
    return cnt

def bfs(x,y,airs,visit,melt):
    q = deque()
    visit[x][y] = True
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        for d in directions:
            nx,ny = cx+d[0],cy+d[1]
            if not check(nx,ny): continue
            # 치즈면 다음 탐색
            if arr[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx,ny))
            if airs[nx][ny]:
                melt.append((cx,cy))

# 구멍이라는 걸 판별하는 방법? -> 공기는 경계와 맞닿아있다.
while True:
    cnt = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1: cnt += 1
    if cnt == 0: break
    rest = cnt

    # 만약 탐색할 치즈가 없다면 break
    airs = [[False] * c for _ in range(r)]
    total_a = 0
    total_c = 0
    for i in range(r):
        if arr[i][0] == 0 and not airs[i][0]:
            total_a += get_air(i,0,airs)
        if arr[i][c-1] == 0 and not airs[i][c-1]:
            total_a += get_air(i,c-1,airs)
        
    for j in range(c):
        if arr[0][j] == 0 and not airs[0][j]:
            total_a += get_air(0,j,airs)
        if arr[r-1][j] == 0 and not airs[r-1][j]:
            total_a += get_air(r-1,j,airs)

    visit = [[False] * c for _ in range(r)]
    melt = []

    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1 and not visit[i][j]:
                bfs(i,j,airs,visit,melt)

    # 테두리 녹이기
    for x,y in melt:
        arr[x][y] = 0
    ans += 1


print(ans)
print(rest)