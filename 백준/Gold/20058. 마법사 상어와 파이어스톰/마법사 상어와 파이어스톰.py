from sys import stdin as input
from collections import deque
# arr[i][j] == 0이면 얼음 x
# 파이어스톰은 격자를 2**l*2**l 크기의 부분 격자로 나눔. 해당 격자를 시계방향 90도 회전
# 이후 해당 격자를 순회하면서 근처에 얼음이 3개 미만으로 있는 칸은 얼음 - 1
n,q = map(int,input.readline().split())
l = 2**n
arr = [list(map(int,input.readline().split())) for _ in range(l)]
cmd = list(map(int,input.readline().split()))
directions = [(0,1),(1,0),(0,-1),(-1,0)]

def check(x,y):
    return 0 <= x < l and 0 <= y < l

def rotate_90(sx,sy,length):
    global arr
    new_arr = [[0] * l for _ in range(l)]
    for x in range(sx,sx+length):
        for y in range(sy,sy+length):
            # 1. (0,0)으로 상대 좌표 옮기기
            ox,oy = x - sx, y - sy
            # 2. 90도 회전 시, 좌표
            rx,ry = oy, length - ox - 1
            new_arr[sx+rx][sy+ry] = arr[x][y]
    # 3. 다시 arr에 옮기기
    for x in range(sx,sx+length):
        for y in range(sy,sy+length):
            arr[x][y] = new_arr[x][y]

def get_melt(arr):
    result = []
    for i in range(l):
        for j in range(l):
            cnt = 0
            for d in directions:
                nx,ny = i + d[0], j + d[1]
                if not check(nx,ny): continue
                if arr[nx][ny] > 0: cnt += 1
            if cnt < 3: result.append((i,j))
    return result

for i in cmd:
    # 모든 격자를 2**i 크기로 나눠야한다.
    for x in range(0,l,2**i):
        for y in range(0,l,2**i):
            # 회전 시뮬레이션
            rotate_90(x,y,2**i)
    # 인접 얼음 3개 있는지 확인
    melt = get_melt(arr)
    for x,y in melt:
        arr[x][y] -= 1

def bfs(x,y,visit):
    global arr
    visit[x][y] = True
    q = deque()
    size = 1
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        for d in directions:
            nx,ny = cx + d[0], cy + d[1]
            if not check(nx,ny): continue
            if arr[nx][ny] > 0 and not visit[nx][ny]:
                size += 1
                visit[nx][ny] = True
                q.append((nx,ny))
    return size

total = 0
max_size = 0
visit = [[False] * l for _ in range(l)]
for i in range(l):
    for j in range(l):
        if arr[i][j] > 0: total += arr[i][j]
        if not visit[i][j] and arr[i][j] > 0:
            max_size = max(max_size, bfs(i,j,visit))

print(total)
print(max_size)