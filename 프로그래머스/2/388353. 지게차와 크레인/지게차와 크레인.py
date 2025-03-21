from collections import deque
def solution(store, rqs):
    arr = []
    ans = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for s in store:
        row = list()
        for c in s:
            row.append(c)
        arr.append(row)
    n = len(arr)
    m = len(arr[0])
    def check(x,y):
        return 0 <= x < n and 0 <= y < m
    
    def bfs(x,y,map):
        q = deque()
        visit = [[False] * m for _ in range(n)]
        visit[x][y] = True
        q.append((x,y))
        while q:
            cx,cy = q.popleft()
            for i in range(4):
                nx,ny = cx + dx[i], cy + dy[i]
                if not check(nx,ny):
                    return True
                if not visit[nx][ny] and map[nx][ny] == 0:
                    visit[nx][ny] = True
                    q.append((nx,ny))
        return False
    
    def removeAll(con):
        for i in range(n):
            for j in range(m):
                if arr[i][j] == con:
                    arr[i][j] = 0
                
    def removeOutSide(con,arr):
        # 처음부터 바깥 혹은 0과 맞대고 있어야 함
        # 순서대로 치우다가 0을 맞댄 녀석이면 해당되지 않는다!
        # 이전과 비교를 할 map 복사
        map = [row[:] for row in arr]
        for i in range(n):
            for j in range(m):
                if arr[i][j] == con:
                    result = bfs(i,j,map)
                    if result:
                        arr[i][j] = 0
    
    for request in rqs:
        # request 길이가 1이면 4면이 바깥 or 0인 거
        if len(request) > 1:
            removeAll(request[0])
        else:
            removeOutSide(request[0],arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                ans += 1
    print(ans)
    return ans