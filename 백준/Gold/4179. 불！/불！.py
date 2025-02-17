from sys import stdin as input
from collections import deque

r,c = map(int, input.readline().split())
q = deque()
arr = []
visit = [[False] * c for _ in range(r)]
for _ in range(r):
    i = list(input.readline().strip())
    arr.append(i)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

jx = 0
jy = 0

fireplace = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            jx = i
            jy = j
        if arr[i][j] == 'F':
            fireplace.append((i, j))

visit[jx][jy] = True

escape = False
ans = 0

def check(x, y):
    return 0 <= x < r and 0 <= y < c
# 불이 간 곳은 지훈이가 가질 못함(visit 공유)
# 불에 대한 bfs를 먼저 진행 후, 지훈에 대한 bfs 진행
# 지훈이가 탈출했음을 나타내는 flag를 세우고 bfs 진행 후
# 탈출했으면 시간 출력 아니면 impossible
def bfs(jx, jy, fireplace):
    global escape
    global ans
    # 불부터 드간다
    for fire in fireplace:
        q.append((0, fire[0], fire[1]))
        visit[fire[0]][fire[1]] = True
    q.append((1, jx, jy))
    while q:
        if escape: break
        who, nx, ny = q.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            # 주체가 불일 경우
            if who == 0:
                if not check(x, y):
                    continue
                # 방문하지 않고 벽이 아니라면
                if not visit[x][y] and arr[x][y] != '#':
                    visit[x][y] = True
                    q.append((0, x, y))
            # 주체가 지훈일 경우
            if who > 0:
                # 체크되지 않았다면 탈출 성공
                if not check(x, y):
                    escape = True
                    ans = who
                    break
                # 방문 하지 않았고 벽과 불이 아니라면
                if not visit[x][y] and arr[x][y] not in '#F':
                    visit[x][y] = True
                    q.append((who + 1, x, y))
bfs(jx, jy, fireplace)
print(ans if escape else "IMPOSSIBLE")