from collections import deque,defaultdict
def solution(land):
    ans = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    n = len(land)
    m = len(land[0])
    size = defaultdict(int)
    cnt = 1
    def bfs(x,y,cnt):
        s = 1
        q = deque()
        land[x][y] += cnt
        q.append((x,y))
        while q:
            cx,cy = q.popleft()
            for d in directions:
                nx,ny = cx+d[0],cy+d[1]
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                    land[nx][ny] += cnt
                    s += 1
                    q.append((nx,ny))
        size[land[x][y]] = s
        
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                bfs(i,j,cnt)
                cnt += 1
    # land[i][j] != 0 -> 시추 번호
    for j in range(m):
        visit = set()
        amount = 0
        # 열을 순회하면서 판단하기
        for i in range(n):
            # 이미 시추한 적이 있다면 pass
            if land[i][j] != 0 and land[i][j] not in visit:
                amount += size[land[i][j]]
                visit.add(land[i][j])
        ans = max(ans,amount)
    return ans