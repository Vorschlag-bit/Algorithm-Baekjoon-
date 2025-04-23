from sys import stdin as input
from collections import deque
r,c = map(int,input.readline().split())
arr = []
d = [(0,1),(1,0),(0,-1),(-1,0)]
for i in range(r):
    row = list(map(str,input.readline().rstrip()))
    arr.append(row)
n = int(input.readline().rstrip())
m = list(map(int,input.readline().split()))

def check(x,y):
    return 0<= x < r and 0<= y < c

def bfs(x,y):
    q = deque()
    visit[x][y] = True
    maxH = x
    cluster = []
    cluster.append((x,y))
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        maxH = max(maxH,cx)
        for i in range(4):
            nx,ny = cx + d[i][0], cy + d[i][1]
            if not check(nx,ny): continue
            if not visit[nx][ny] and arr[nx][ny] == 'x':
                visit[nx][ny] = True
                q.append((nx,ny))
                cluster.append((nx,ny))
    if maxH != r-1:
        return cluster,True
    else: return cluster,False

def gravity(cluster):
    for i,j in cluster:
        arr[i][j] = '.'

    h = 1
    while True:
        flag = True
        for i,j in cluster:
            new_i = i + h
            if new_i >= r or arr[new_i][j] == 'x':
                flag = False
                break
        if not flag:
            h -= 1
            break
        h += 1
    
    for i,j in cluster:
        arr[i+h][j] = 'x'
        visit[i+h][j] = True


for idx,t in enumerate(m):
    # 짝수번은 왼쪽
    t -= 1
    if idx % 2 == 0:
        for j in range(c):
            if arr[r-1-t][j] == 'x':
                arr[r-1-t][j] = '.'
                break
    # 홀수번은 오른쪽
    else:
        for j in range(c-1,-1,-1):
            if arr[r-1-t][j] == 'x':
                arr[r-1-t][j] = '.'
                break
    
    visit = [[False] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not visit[i][j] and arr[i][j] == 'x':
                cluster,flag = bfs(i,j)
                if flag:
                    gravity(cluster)

for i in range(r):
    print(''.join(arr[i]))