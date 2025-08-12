from sys import stdin as input
from collections import deque
ans = 0
r,c,t = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(r)]
clean = [0,0]
for i in range(r):
    if arr[i][0] == -1:
        clean[0] = i
        clean[1] = i+1
        break

directions = [(0,1),(1,0),(0,-1),(-1,0)]

for _ in range(t):
    # 미세먼지 확산
    dust = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] > 0:
                # 확산되는 양
                cnt = 0
                spread = arr[x][y] // 5
                for d in directions:
                    nx,ny = x+d[0], y+d[1]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        dust[nx][ny] += spread
                        cnt += 1
                arr[x][y] -= spread * cnt
    for i in range(r):
        for j in range(c):
            if arr[i][j] != -1: arr[i][j] += dust[i][j]

    # 바람 불기(위: 반시계)
    c1 = clean[0]
    # ->
    ex = 0
    for j in range(1,c):
        temp = arr[c1][j]
        arr[c1][j] = ex
        ex = temp
    # 위
    for i in range(c1-1,-1,-1):
        temp = arr[i][c-1]
        arr[i][c-1] = ex
        ex = temp
    # <-
    for j in range(c-2,-1,-1):
        temp = arr[0][j]
        arr[0][j] = ex
        ex = temp
    # 아래
    for i in range(1,c1):
        temp = arr[i][0]
        arr[i][0] = ex
        ex = temp

    # 바람 불기(아래: 시계)
    c2 = clean[1]
    ex = 0
    # ->
    for j in range(1,c):
        temp = arr[c2][j]
        arr[c2][j] = ex
        ex = temp
    # 아래
    for i in range(c2+1,r):
        temp = arr[i][c-1]
        arr[i][c-1] = ex
        ex = temp
    # <-
    for j in range(c-2,-1,-1):
        temp = arr[r-1][j]
        arr[r-1][j] = ex
        ex = temp
    # 위
    for i in range(r-2,c2,-1):
        temp = arr[i][0]
        arr[i][0] = ex
        ex = temp

for i in range(r):
    for j in range(c):
        if arr[i][j] > 0: ans += arr[i][j]

print(ans)