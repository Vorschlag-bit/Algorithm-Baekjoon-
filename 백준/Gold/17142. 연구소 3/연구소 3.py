from sys import stdin as input
from collections import deque
n,m = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
# 0: 빈칸, 1: 벽, 2: 바이러스
virus = []
walls = []
empty = 0
directions = [(0,1),(1,0),(0,-1),(-1,0)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 1:
            walls.append((i,j))
        else: empty += 1

def comb(array,r):
    result = []
    def dfs(idx,path,r,array):
        nonlocal result
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(idx,len(array)):
            path.append(array[i])
            dfs(i+1,path,r,array)
            path.pop()
    dfs(0,[],r,array)
    return result
ans = float('inf')
for c in comb(virus,m):
    visit = [[False] * n for _ in range(n)]
    q = deque()
    flag = False
    remain = empty
    for x,y in c:
        q.append((0,x,y))
        visit[x][y] = True
    for x,y in walls:
        visit[x][y] = True
    last_t = 0
    while q and remain > 0:
        time,cx,cy = q.popleft()
        for d in directions:
            nx,ny = cx + d[0], cy + d[1]
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    if arr[nx][ny] == 0:
                        remain -= 1
                        last_t = time+1
                    q.append((time+1,nx,ny))
    if remain == 0: ans = min(ans,last_t)
print(ans if ans != float('inf') else -1)