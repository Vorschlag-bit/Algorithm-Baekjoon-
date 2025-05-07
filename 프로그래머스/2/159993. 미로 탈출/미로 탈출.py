from collections import deque
def solution(arr):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    ans = 0
    lx,ly = 0,0
    sx,sy = 0,0
    ex,ey = 0,0
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'L':
                lx,ly = i,j
            if arr[i][j] == 'S':
                sx,sy = i,j
            if arr[i][j] == 'E':
                ex,ey = i,j
    def bfs(x,y,t):
        target = 'L' if t == 0 else 'E'
        q = deque()
        visit = [[False]*m for _ in range(n)]
        visit[x][y] = True
        q.append((x,y,0))
        while q:
            cx,cy,step = q.popleft()
            if arr[cx][cy] == target:
                return step
            for i in range(4):
                nx,ny = cx+direction[i][0],cy+direction[i][1]
                if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and arr[nx][ny] != 'X':
                    visit[nx][ny] = True
                    q.append((nx,ny,step+1))
        return 0
    tol = bfs(sx,sy,0)
    if tol == 0: return -1
    toe = bfs(lx,ly,1)
    if toe == 0: return -1
    return tol+toe