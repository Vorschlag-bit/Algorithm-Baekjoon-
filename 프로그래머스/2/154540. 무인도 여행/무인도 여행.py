from collections import deque
def solution(arr):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    ans = []
    n = len(arr)
    m = len(arr[0])
    visit = [[False]*m for _ in range(n)]
    def bfs(x,y):
        nonlocal visit
        q = deque()
        visit[x][y] = True
        q.append((x,y))
        s = int(arr[x][y])
        while q:
            cx,cy = q.popleft()
            for i in range(4):
                nx,ny = cx+direction[i][0],cy+direction[i][1]
                if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and arr[nx][ny] != 'X':
                    visit[nx][ny] = True
                    s += int(arr[nx][ny])
                    q.append((nx,ny))
        print(s)
        return s
        
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and arr[i][j] != 'X':
                ans.append(bfs(i,j))
    return [-1] if len(ans) == 0 else sorted(ans)