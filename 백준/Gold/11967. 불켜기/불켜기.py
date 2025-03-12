from collections import deque
from sys import stdin as input

n,m = map(int, input.readline().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [[False for _ in range(n+1)] for _ in range(n+1)]
dic = dict()
for i in range(m):
    x,y,a,b = map(int, input.readline().split())
    dic.setdefault((x,y), []).append((a,b))

def check(x,y):
    return 1 <= x <= n and 1 <= y <= n
ans = 1
def bfs(i,j):
    global ans
    q = deque()
    q.append((i,j))
    arr[i][j] = 1
    visit[i][j] = True
    while q:
        x,y = q.popleft()
        for d in range(4):
            # 현재 방에서 근처에 켜지고 방문한 적이 없다면 q에 쌓기
            nx,ny = x + dx[d], y + dy[d]
            if check(nx,ny) and arr[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx,ny))
        v = dic.get((x,y), [])
        for a,b in v:
            if arr[a][b] == 0:
                arr[a][b] = 1
                ans += 1
                for d in range(4):
                    nx,ny = a + dx[d], b + dy[d]
                    if check(nx,ny) and visit[nx][ny]:
                        visit[a][b] = True
                        q.append((a,b))
                        break

bfs(1,1)
print(ans)