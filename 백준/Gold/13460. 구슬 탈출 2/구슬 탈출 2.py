from collections import deque
from sys import stdin as input

n,m = map(int, input.readline().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
arr = [list(map(str, input.readline().rstrip())) for _ in range(n)]
visit = []
rx,ry = 0,0
bx,by = 0,0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx,ry = i,j
        if arr[i][j] == 'B':
            bx,by = i,j
# 두 구슬을 동시에 같은 곳에 위치할 수 없다
# 두 구슬은 이동할 때마다 벽인지, 구멍인지를 확인해야 한다.
def bfs(rx,ry,bx,by):
    q = deque()
    visit.append((rx,ry,bx,by))
    q.append((rx,ry,bx,by,0))
    while q:
        ax,ay,cx,cy,cnt = q.popleft()
        if cnt > 10:
            print(-1)
            exit()
        if arr[ax][ay] == 'O':
            print(cnt)
            exit()
        for i in range(4):
            nrx,nry = ax,ay
            nbx,nby = cx,cy
            # 구슬을 끝까지 이동
            while True:
                nrx += dx[i]
                nry += dy[i]
                if arr[nrx][nry] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                if arr[nrx][nry] == 'O':
                    break
            while True:
                nbx += dx[i]
                nby += dy[i]
                if arr[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                if arr[nbx][nby] == 'O':
                    break
            if arr[nbx][nby] == 'O':
                continue
            if nrx == nbx and nry == nby:
                if abs(nrx - ax) + abs(nry -ay) > abs(nbx - cx) + abs(nby - cy):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if (nrx,nry,nbx,nby) not in visit:
                visit.append((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,cnt+1))
    print(-1)

bfs(rx,ry,bx,by)