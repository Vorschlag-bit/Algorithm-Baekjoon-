from sys import stdin as input
from collections import deque

n = int(input.readline())
directions = [(-1,0),(0,-1),(1,0),(0,1)]  # 상, 좌, 하, 우 (우선순위 순서)
arr = [list(map(int,input.readline().split())) for _ in range(n)]
shark = (0,0)
ss = 2  # 상어 크기

# 상어 초기 위치 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9: 
            shark = (i,j)
            arr[i][j] = 0
            break

ans = 0
ate = 0

def check(x,y):
    return 0 <= x < n and 0 <= y < n

def get():
    global ans, ate, ss, shark
    q = deque()
    visit = [[False] * n for _ in range(n)]
    x, y = shark
    visit[x][y] = True
    can = []
    q.append((x, y, 0))
    
    while q:
        cx, cy, dis = q.popleft()
        for d in directions:
            nx, ny = cx + d[0], cy + d[1]
            if not check(nx, ny) or visit[nx][ny]: 
                continue
            
            # 자신보다 큰 물고기가 있는 칸은 지날 수 없음
            if arr[nx][ny] > ss: 
                continue
            
            visit[nx][ny] = True
            
            # 먹을 수 있는 물고기인지 확인 (크기가 0보다 크고 상어보다 작음)
            if 0 < arr[nx][ny] < ss:
                can.append((dis + 1, nx, ny))
            else:
                # 지나갈 수 있는 칸이면 큐에 추가
                q.append((nx, ny, dis + 1))
    
    # 거리, 행, 열 순으로 정렬
    can.sort(key=lambda x: (x[0], x[1], x[2]))
    return can

while True:
    result = get()
    if len(result) == 0:
        break
    
    # 가장 우선순위가 높은 물고기 먹기
    dis, x, y = result[0]
    arr[x][y] = 0 
    ate += 1
    ans += dis
    shark = (x, y)
    
    # 상어 크기만큼 먹으면 크기 증가
    if ate == ss:
        ss += 1
        ate = 0

print(ans)