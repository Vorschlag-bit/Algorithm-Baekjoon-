from sys import stdin as input

n = int(input.readline())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
sx, sy = n // 2, n // 2

# 이동방향: 좌, 하, 우, 상
directions = [(0,-1), (1,0), (0,1), (-1,0)]
pattern = [(-2,0,0.02),(2,0,0.02),(-1,-1,0.1),(1,-1,0.1),
           (1,0,0.07),(-1,0,0.07),(1,1,0.01),(-1,1,0.01),
           (0,-2,0.05)]

# 격자 범위 확인 함수
def check(x, y):
    return 0 <= x < n and 0 <= y < n

def simulate(x,y,idx):
    global ans,arr,pattern
    sand = arr[x][y]
    if sand == 0: return
    # 뿌려진 모래
    lost = 0
    for dx,dy,p in pattern:
        # 좌
        if idx == 0:
            nx,ny = x + dx, y + dy
        # 하
        elif idx == 1:
            nx,ny = x - dy, y + dx
        # 우
        elif idx == 2:
            nx,ny = x - dx, y - dy
        # 상
        else:
            nx,ny = x + dy, y - dx
        # 흩어질 모래
        ss = int(arr[x][y] * p)
        if check(nx,ny): arr[nx][ny] += ss
        else: ans += ss
        lost += ss
    rest = sand - lost
    # a위치
    ax,ay = x + directions[idx][0], y + directions[idx][1]
    if check(ax,ay): arr[ax][ay] += rest
    else: ans += rest
    arr[x][y] = 0

ans = 0
dis = 1  # 이동 거리
idx = 0  # 방향 인덱스
num = 0  # 이동한 칸 수

while num < n * n:
    for _ in range(2):
        for _ in range(dis):
            nx, ny = sx + directions[idx][0], sy + directions[idx][1]
            if not check(nx, ny):
                num = n * n
                break
            simulate(nx, ny, idx)
            sx, sy = nx, ny
            num += 1
        idx = (idx+1)%4
        if num == n*n: break
    dis += 1
print(ans)