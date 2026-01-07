from sys import stdin as input
from collections import deque

n,m = map(int,input.readline().split())
directions = [(0,1),(1,0),(-1,0),(0,-1)]
nd = { 'D':1, 'U':2, 'L':3, 'R':0 }
# 1000 * 1000 = 1000000(백만)
# bfs
visit = [[-1] * m for _ in range(n)]
ans = 0
arr = []
for _ in range(n):
    arr.append(list(map(str,input.readline().strip())))

def check(x,y): return 0 <= x < n and 0 <= y < m

def bfs(sx,sy,num):
    q = deque()
    visit[sx][sy] = num
    q.append((sx,sy))
    # 이전에 있던 집합과 연결되었는지를 판단해줄 flag
    flag = False
    while q:
        cx,cy = q.popleft()
        d = nd[arr[cx][cy]]
        nx,ny = cx + directions[d][0], cy + directions[d][1]
        if not check(nx,ny): continue
        if visit[nx][ny] == num: continue
        if visit[nx][ny] != num and visit[nx][ny] != -1: 
            flag = True
            continue
        visit[nx][ny] = num
        q.append((nx,ny))
    return flag

cnt = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == -1:
            ans += 1
            cnt += 1
            # 이미 존재하는 집합과 연결되는 거면 -1
            if bfs(i,j,cnt): ans -= 1

print(ans)