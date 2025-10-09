from collections import deque

def check(x,y,n): return 0 <= x < n and 0 <= y < n

def solution(board):
    # 우,하,좌,상 순
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    n = len(board)
    # 상하좌우로 해당 칸 입성할 때 최솟값
    visit = [[[float('inf')] * n for _ in range(n)] for _ in range(4)]
    q = deque()
    # 아래 방향
    # x,y,dir,cost
    q.append((0,0,1,0))
    # 오른쪽 방향
    q.append((0,0,0,0))
    visit[1][0][0] = 0
    visit[0][0][0] = 0
    while q:
        cx,cy,cd,cost = q.popleft()
        for i,d in enumerate(directions):
            nx,ny = cx + d[0], cy + d[1]
            if not check(nx,ny,n) or board[nx][ny] == 1: continue
            # 우 하 상 좌
            # 현재 방향과 일치 -> 100
            if cd == i or (cd+2) % 4 == i:
                # 최소 금액이 아니라면 pass
                if visit[i][nx][ny] <= cost + 100: continue
                visit[i][nx][ny] = cost + 100
                q.append((nx,ny,i,cost+100))
            # 코너 -> 600
            else:
                # 최소 금액 아니라면 pass
                if visit[i][nx][ny] <= cost + 600: continue
                visit[i][nx][ny] = cost + 600
                q.append((nx,ny,i,cost+600))
    ans = float('inf')
    for i in range(4):
        ans = min(ans,visit[i][n-1][n-1])
    return ans