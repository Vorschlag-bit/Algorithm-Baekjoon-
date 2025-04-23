from sys import stdin as input
from collections import defaultdict,deque
n,k,r = map(int,input.readline().split())
graph = defaultdict(list)
direction = [(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(r):
    r1,c1,r2,c2 = map(int,input.readline().split())
    graph[(r1-1,c1-1)].append((r2-1,c2-1))
    graph[(r2-1,c2-1)].append((r1-1,c1-1))
cow = []
for _ in range(k):
    x,y = map(int,input.readline().split())
    cow.append((x-1,y-1))

def check(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y,id):
    q = deque()
    arr[x][y] = id
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        for d in range(4):
            nx,ny = cx+direction[d][0],cy+direction[d][1]
            if not check(nx,ny): continue
            if arr[nx][ny] == -1 and (nx,ny) not in graph[(cx,cy)]:
                q.append((nx,ny))
                arr[nx][ny] = id
arr = [[-1] * n for _ in range(n)]
id = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == -1:
            bfs(i,j,id)
            id += 1
cow_id = []
for c in cow:
    id = arr[c[0]][c[1]]
    cow_id.append(id)
ans = 0
for i in range(len(cow_id)):
    for j in range(i+1,len(cow_id)):
        if cow_id[i] != cow_id[j]:
            ans += 1
print(ans)