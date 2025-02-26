from collections import deque
from sys import stdin as input

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input.readline().rstrip())

def check(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

for _ in range(t):
    m, n = map(int, input.readline().split())
    arr = []
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        row = list(input.readline().rstrip())
        arr.append(row)
    fire = []
    q = deque()
    si = 0
    sj = 0
    for i in range(n):
        for j in  range(m):
    # 불 먼저 bfs
            if arr[i][j] == '*':
                q.append((i, j, -1))
                visit[i][j] = True
            elif arr[i][j] == '@':
                si = i
                sj = j
    # 상근이 q에 넣기
    visit[si][sj] = True
    q.append((si, sj, 0))
    ans = "IMPOSSIBLE"
    flag = False
    while q and not flag:
        cx, cy, s = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 주체가 불일 경우
            if s < 0:
                if not check(nx, ny, n, m): continue
                # 벽만 아니라면 bfs
                if arr[nx][ny] != '#' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny, -1))
            # 주체가 상근이인 경우
            else:
                if not check(nx, ny, n, m):
                    ans = s + 1
                    flag = True
                    break
                elif arr[nx][ny] not in '#*' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx ,ny, s + 1))
    print(ans)