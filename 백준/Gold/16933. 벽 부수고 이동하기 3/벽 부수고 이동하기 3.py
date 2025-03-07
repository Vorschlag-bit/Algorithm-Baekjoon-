from collections import deque
from sys import stdin as input

n,m,k = map(int, input.readline().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = [list(map(int, input.readline().rstrip())) for _ in range(n)]
# 낮(밤), n, m
visit = [[(float('inf'))] * m for _ in range(n)]

q = deque()
def check(x,y):
    return 0<= x < n and 0<= y < m
# 거리, 시간, 횟수, x, y
q.append((1, 0, 0, 0, 0))
visit[0][0] = 0

while q:
    dis, t, cnt, x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(dis)
        exit()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not check(nx,ny): continue
        time = 1 if t == 0 else 0
        # 벽이 아닌 곳은 일단 다 이동가능
        if arr[nx][ny] != 1 and visit[nx][ny] > cnt:
            visit[nx][ny] = cnt
            q.append((dis+1, time, cnt, nx, ny))
        # 벽이라면, 낮일 때는 cnt 체크 후 이동, 아니면 
        if arr[nx][ny] == 1:
            if cnt == k: continue
            # 최소의 벽 부수기 저장
            if t == 0 and visit[nx][ny] > cnt+1:
                visit[nx][ny] = cnt + 1
                q.append((dis+1, 1, cnt+1, nx, ny))
            elif t == 1:
                q.append((dis+1, 0, cnt, x, y))
print(-1)
