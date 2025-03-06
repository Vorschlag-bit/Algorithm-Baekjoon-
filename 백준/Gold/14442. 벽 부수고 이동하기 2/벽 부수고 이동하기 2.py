from collections import deque
from sys import stdin as input

n, m, k = map(int, input.readline().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
arr = [list(map(int, input.readline().rstrip())) for _ in range(n)]
dis = [[[0] * m for _ in range(n)] for _ in  range(k+1)]
def check(x,y):
    return 0<= x < n and 0<= y < m
q = deque()
dis[0][0][0] = 1
q.append((0,0,0))
while q:
    cnt, x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(dis[cnt][x][y])
        exit()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not check(nx,ny): continue
        # 벽이 아닌 경우
        if arr[nx][ny] == 0:
            if dis[cnt][nx][ny] == 0:
                dis[cnt][nx][ny] = dis[cnt][x][y] + 1
                q.append((cnt,nx,ny))
        # 벽인 경우
        else:
            # 부술 기회가 있고
            if cnt < k:
                # 방문한 적이 없다면
                if dis[cnt+1][nx][ny] == 0:
                    dis[cnt+1][nx][ny] = dis[cnt][x][y] + 1
                    q.append((cnt+1,nx,ny))
print(-1)