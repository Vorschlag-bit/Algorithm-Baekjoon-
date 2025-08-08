import heapq
def solution(land, height):
    ans = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    n = len(land)
    visit = [[False] * n for _ in range(n)]
    q = [(0,0,0)]
    while q:
        cost,i,j = heapq.heappop(q)
        if visit[i][j]: continue
        visit[i][j] = True
        ans += cost
        for d in directions:
            nx,ny = i+d[0], j+d[1]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                diff = abs(land[i][j] - land[nx][ny])
                if diff <= height:
                    heapq.heappush(q,(0,nx,ny))
                else:
                    heapq.heappush(q,(diff,nx,ny))
    return ans