from collections import deque
from sys import stdin as input

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input.readline().rstrip())

arr = []
for _ in range(n):
    i = list(map(int, input.readline().split()))
    arr.append(i)

maxh = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > maxh:
            maxh = arr[i][j]

ans = 0

def check(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y, h):
    q = deque()
    visit[x][y] = True
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not check(nx, ny): continue
            if not visit[nx][ny] and arr[nx][ny] > h:
                visit[nx][ny] = True
                q.append((nx, ny))


# 모든 지역이 안 잠길 수 있다는 의미는 아마도
# 비가 아예 안 올 수도 있다 or 반드시 정수단위로 오는 건 아니다(0.5)
for h in range(0, maxh + 1):
    visit = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visit[i][j]:
                bfs(i, j, h)
                cnt += 1
    ans = max(ans, cnt)

print(ans)