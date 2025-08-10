from sys import stdin as input
from collections import deque
directions = [(1,0),(0,1),(-1,0),(0,-1)]
n,l,r = map(int,input.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input.readline().split())))

def bfs(x,y,visit):
    q = deque()
    q.append((x,y))
    visit[x][y] = True
    total = arr[x][y]
    c = [(x,y)]
    while q:
        cx,cy = q.popleft()
        for d in directions:
            nx,ny = cx + d[0], cy + d[1]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                diff = abs(arr[nx][ny] - arr[cx][cy])
                if l <= diff <= r:
                    visit[nx][ny] = True
                    total += arr[nx][ny]
                    c.append((nx,ny))
                    q.append((nx,ny))
    return c,total

ans = 0
while True:
    visit = [[False] * n for _ in range(n)]
    update = []

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                c,total = bfs(i,j,visit)
                # 연합이 존재한다면
                if len(c) > 1:
                    avg = total // len(c)
                    update.append((c,avg))
    
    if not update: break

    for c,avg in update:
        for x,y in c:
            arr[x][y] = avg
    ans += 1
print(ans)