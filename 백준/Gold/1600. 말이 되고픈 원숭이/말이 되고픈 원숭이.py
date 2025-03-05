from collections import deque
from sys import stdin as input

k = int(input.readline().rstrip())

m,n = map(int, input.readline().split())
arr = [list(map(int, input.readline().split())) for _ in range(n)]
# k를 최소 횟수로 사용하여 최단 거리를 저장하는 배열
visit = [[[(m*n+1)] * m for _ in range(n)] for _ in range(k+1)]
ans = m*n+1
dx = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, -1, 0, 0, -1, -2, -2, -1, 1, 2, 2, 1]
q = deque()
q.append((0,k,0,0,))
visit[k][0][0] = 0
def check(x,y):
    return 0<= x < n and 0<= y < m
flag = False
while q:
    s, h, x, y = q.popleft()
    if x == n-1 and y == m-1:
        flag = True
    # 우선 4방향
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not check(nx,ny): continue
        if arr[nx][ny] != 1 and visit[h][nx][ny] > s + 1:
            visit[h][nx][ny] = s + 1
            q.append((s+1,h,nx,ny))
    # 말의 움직임이 남아있다면
    if h > 0:
        for i in range(4,12):
            nx = x + dx[i]
            ny = y + dy[i]
            if not check(nx,ny): continue
            if arr[nx][ny] != 1 and visit[h-1][nx][ny] > s + 1:
                visit[h-1][nx][ny] = s + 1
                q.append((s+1,h-1,nx,ny))
if flag:
    for i in range(k+1):
        if ans > visit[i][n-1][m-1]:
            ans = visit[i][n-1][m-1]
print(ans if flag else -1)