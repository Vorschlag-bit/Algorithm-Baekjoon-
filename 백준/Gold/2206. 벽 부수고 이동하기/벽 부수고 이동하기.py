from collections import deque
from sys import stdin as input

n, m = map(int, input.readline().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 아이디어: 방문 배열을 3차원 배열로 생성하여, 벽을 부술 때와 안 부술 때의 최솟값을 저장.
# visit[2][n][m]
arr = [list(map(int, input.readline().rstrip())) for _ in range(n)]
visit = [[[10000 for _ in range(m)] for _ in range(n)] for _ in range(2)]

def check(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(i, j):
    q = deque()
    # visit[0][i][j] <= 벽을 안 부수고 도착할 때의 최솟값
    # visit[1][i][j] <= 벽을 부수고 도착할 때의 최솟값
    visit[0][i][j] = 1  # 시작점은 벽을 부수지 않은 상태로 1
    # (x, y, 벽을 부술 수 있는지 여부)
    q.append((i, j, 0))  # 처음에는 벽을 부수지 않은 상태(0)
    
    while q:
        cx, cy, wall = q.popleft()
        
        # 목적지에 도착했으면 현재까지의 거리 반환
        if cx == n - 1 and cy == m - 1:
            return visit[wall][cx][cy]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if not check(nx, ny): 
                continue
                
            # 다음 칸이 벽이 아니면
            if arr[nx][ny] == 0:
                # 아직 방문하지 않았으면 (현재 상태에서)
                if visit[wall][nx][ny] == 10000:
                    visit[wall][nx][ny] = visit[wall][cx][cy] + 1
                    q.append((nx, ny, wall))
            # 다음 칸이 벽이고, 아직 벽을 부수지 않았으면
            elif arr[nx][ny] == 1 and wall == 0:
                # 벽을 부순 상태로 방문하지 않았으면
                if visit[1][nx][ny] == 10000:
                    visit[1][nx][ny] = visit[0][cx][cy] + 1
                    q.append((nx, ny, 1))
    
    # 목적지에 도달할 수 없는 경우
    return -1

ans = bfs(0, 0)
print(ans)