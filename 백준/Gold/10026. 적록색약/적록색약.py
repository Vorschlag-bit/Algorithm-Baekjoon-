from sys import stdin as input
from collections import deque

n = int(input.readline().strip())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()
arr = []
visit = [[False] * n for _ in range(n)]

for _ in range(n):
    row = list(input.readline().strip())
    arr.append(row)

nor = 0
abn = 0

def check(x, y):
    return 0 <= x < n and 0 <= y < n

# 적록색약을 위한 bfs
def abnormal(x, y, char):
    visit[x][y] = True
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not check(nx, ny): continue
            # char가 'R'이나 'G'인 경우
            if char == 'R' or char == 'G':
                if not visit[nx][ny] and arr[nx][ny] in 'RG':
                    visit[nx][ny] = True
                    q.append((nx, ny))
            # char가 'B'인 경우
            else:
                if not visit[nx][ny] and arr[nx][ny] == char:
                    visit[nx][ny] = True
                    q.append((nx, ny))

# 일반인을 위한 bfs
def normal(x, y, char):
    visit[x][y] = True
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not check(nx, ny): continue
            if not visit[nx][ny] and arr[nx][ny] == char:
                visit[nx][ny] = True
                q.append((nx, ny))

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            normal(i, j, arr[i][j])
            nor += 1
# 방문 배열 초기화
visit = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            abnormal(i, j, arr[i][j])
            abn += 1

print(str(nor) + " " + str(abn))