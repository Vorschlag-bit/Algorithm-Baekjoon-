from collections import deque
from sys import stdin as input

n, m, k = map(int, input.readline().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
arr = [list(map(int, input.readline().rstrip())) for _ in range(n)]
visit = [[k+1] * m for _ in range(n)]
def check(x,y):
    return 0<= x < n and 0<= y < m
q = deque()
visit[0][0] = 0
# 거리, 횟수, x, y
q.append((1,0,0,0))
while q:
    dis, cnt, x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(dis)
        exit()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not check(nx,ny): continue
        # 기존 방문 배열보다 더 적게 벽을 부수고 왔다면
        if arr[nx][ny] + cnt < visit[nx][ny]:
            visit[nx][ny] = arr[nx][ny] + cnt
            q.append((dis+1,visit[nx][ny],nx,ny))
print(-1)