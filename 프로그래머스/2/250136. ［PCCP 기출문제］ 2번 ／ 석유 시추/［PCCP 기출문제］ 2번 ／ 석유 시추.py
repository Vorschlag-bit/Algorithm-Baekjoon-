from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    id_map = [[-1] * m for _ in range(n)]
    ans = 0
    dx,dy = [0,0,1,-1], [1,-1,0,0]
    # n번째 석유가 갖고 있는 총 시추량
    oils = dict()
    node = 0
    def check(x,y):
        return 0 <= x < n and 0 <= y < m
    
    def bfs(x,y,no):
        q = deque([(x,y)])
        visit[x][y] = True
        cnt = 1
        id_map[x][y] = no
        while q:
            cx,cy = q.popleft()
            for i in range(4):
                nx,ny = cx + dx[i], cy + dy[i]
                if not check(nx,ny): continue
                if not visit[nx][ny] and land[nx][ny] == 1:
                    visit[nx][ny] = True
                    id_map[nx][ny] = no
                    cnt += 1
                    q.append((nx,ny))
        oils[no] = cnt
        return
    visit = [[False] * m for _ in range(n)]
    # 석유 매장 맵, 양 dict 초기화
    for j in range(m):
        for i in range(n):
            if land[i][j] == 1 and not visit[i][j]:
                bfs(i,j,node)
                node += 1
    
    for j in range(m):
        oil = 0
        visited = set()
        for i in range(n):
            oil_no = id_map[i][j]
            if oil_no != -1 and oil_no not in visited:
                visited.add(oil_no)
                oil += oils[oil_no]
        ans = max(ans,oil)
    
    return ans