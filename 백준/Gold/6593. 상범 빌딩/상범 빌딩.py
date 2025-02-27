from collections import deque
from sys import stdin as input

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def check(z, x, y, l, r, c):
    return 0 <= x < r and 0 <= y < c and 0 <= z < l

def bfs(z, x, y):
    global ans
    global escape
    # 정답을 내뱉을 때 -1 해주기
    visit[z][x][y] = 1
    q = deque()
    q.append((z, x, y))
    while q:
        cz, cx, cy = q.popleft()
        if arr[cz][cx][cy] == 'E':
            ans = visit[cz][cx][cy] - 1
            escape = True
            break
        for i in range(6):
            nz = cz + dz[i]
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not check(nz, nx, ny, l ,r, c): continue
            # 방문하지 않고 빈 칸이거나  bfs
            if visit[nz][nx][ny] == 0 and arr[nz][nx][ny] in '.E':
                visit[nz][nx][ny] = visit[cz][cx][cy] + 1
                q.append((nz, nx, ny))

while True:
    l, r, c = map(int, input.readline().split())
    if l == 0 and r == 0 and c == 0:
        break
    ans = "Trapped!"
    arr = []
    # 빌딩 초기화
    for i in range(l):
        arrH = []
        for j in range(r):
            row = list(input.readline().rstrip())
            arrH.append(row)
        # 빈 한 줄 받기
        blank = input.readline().rstrip()
        arr.append(arrH)
    sz = 0
    sx = 0
    sy = 0
    # 상범 위치 초기화
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    sz = i
                    sx = j
                    sy = k
    # 방문배열 초기화
    visit = [[[0] * c for _ in range(r)] for _ in range(l)]
    escape = False
    bfs(sz, sx, sy)
    if escape:
        print("Escaped in " + str(ans) + " minute(s).")
    else: print(ans)