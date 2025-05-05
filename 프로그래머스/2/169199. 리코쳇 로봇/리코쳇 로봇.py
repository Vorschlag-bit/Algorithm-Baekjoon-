from collections import deque
def solution(arr):
    ans = -1
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    # 'G'에 정확히 멈추기
    x,y = 0,0
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                x,y = i,j
                break
    visit = [[False]*m for _ in range(n)]
    visit[x][y] = True
    q = deque()
    q.append((x,y,0))
    while q:
        cx,cy,cnt = q.popleft()
        if arr[cx][cy] == 'G':
            ans = cnt
            break
        for i in range(4):
            a,b = cx,cy
            while True:
                nx,ny = a+direction[i][0],b+direction[i][1]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'D':
                    a,b = nx,ny
                else: break
            if not visit[a][b]:
                visit[a][b] = True
                q.append((a,b,cnt+1))
            
    return ans