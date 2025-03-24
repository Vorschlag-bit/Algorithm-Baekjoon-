from collections import deque
# 그리디하게 풀어볼 것(사전순) -> 목표 지점까지 가는 후보군을 설정,
# 후보군의 조건, 사전순으로 제일 빠르며, k - (현재 지점에서 목표지점 맨하튼 거리) = 짝수
def solution(n, m, x, y, r, c, k):
    ans = []
    direction = [(1,0),(0,-1),(0,1),(-1,0)]
    move = ['d','l','r','u']
    visit = [[[False] * (m+1) for _ in range(n+1)] for _ in range(k+1)]
    q = deque()
    def check(a,b):
        return 1<= a < n+1 and 1 <= b < m+1
    
    visit[0][x][y] = 0
    q.append((x,y,0,''))
    while q:
        cx,cy,dis,route = q.popleft()
        if dis == k:
            if cx == r and cy == c:
                ans.append(route)
                continue
            else: continue
        for i in range(4):
            nx,ny = cx + direction[i][0], cy + direction[i][1]
            if not check(nx,ny): continue
            if not visit[dis+1][nx][ny]:
                visit[dis+1][nx][ny] = True
                q.append((nx,ny,dis+1,route + move[i]))
    return ans[0] if ans else "impossible"