from sys import stdin as input
n,m = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
directions = [(0,-1),(1,0),(0,1),(-1,0)]
# 구슬 파괴 주문 방향
md = [(-1,0),(1,0),(0,-1),(0,1)]
# 상어 위치
sx,sy = n//2,n//2
cmd = []
for _ in range(m):
    d,s = map(int,input.readline().split())
    cmd.append((d-1,s))
b1 = 0
b2 = 0
b3 = 0
arr[sx][sy] = -1

def check(x,y):
    return 0 <= x < n and 0 <= y < n

# 토네이도 경로 이미 저장
path = []
def get_path(path):
    global sx,sy
    cx,cy = sx,sy
    idx = 0
    dis = 1
    while len(path) < n**2-1:
        for _ in range(2):
            for _ in range(dis):
                nd = directions[idx]
                nx,ny = cx + nd[0], cy + nd[1]
                if check(nx,ny): path.append((nx,ny))
                cx,cy = nx,ny
            idx = (idx+1)%4
        dis += 1
get_path(path)

def destroy():
    global arr,sx,sy,b1,b2,b3
    # 파괴된 구슬 수
    cnt = 0
    beads = []
    # 연속된 구슬 4개 이상이면 파괴
    for x,y in path:
        if arr[x][y] > 0: beads.append(arr[x][y])
    # 구슬의 idx = path의 idx
    i = 0
    while i < len(path):
        start = i
        cx,cy = path[start]
        color = arr[cx][cy]
        if color == 0: break
        while i < len(path) and color == arr[path[i][0]][path[i][1]]:
            i += 1
        # 길이
        length = i - start
        if length > 3:
            cnt += length
            for idx in range(start,start+length):
                x,y = path[idx]
                if arr[x][y] == 1: b1 += 1
                elif arr[x][y] == 2: b2 += 1
                else: b3 += 1
                arr[x][y] = 0
    return cnt > 0

def move():
    global path,arr
    # 구슬 수집
    beads = []
    for x,y in path:
        if arr[x][y] > 0:
            beads.append(arr[x][y])
        arr[x][y] = 0
    # 구슬 순서대로 배치
    for i,color in enumerate(beads):
        if i < len(path):
            x,y = path[i]
            arr[x][y] = color

def new_number(arr):
    global path
    # 새로 쌓이길 될 구슬들(a,b로 인해서)
    beads = []
    # 그룹 리스트
    i = 0
    while i < len(path):
        # 더 못 넣으면 break
        if i < len(path) and len(beads) > len(path): break
        start = i
        cx,cy = path[start]
        color = arr[cx][cy]
        if color == 0: break
        # 색이 같은 그룹 개수
        while i < len(path) and color == arr[path[i][0]][path[i][1]]:
            i += 1
        length = i - start
        # a
        beads.append(length)
        # b
        beads.append(color)

        if len(beads) >= len(path): break

    for x,y in path:
        arr[x][y] = 0
    
    # 구슬 다시 채우기
    m = min(len(path),len(beads))
    for idx in range(m):
        x,y = path[idx]
        color = beads[idx]
        arr[x][y] = color

for d,s in cmd:
    # 구슬 파괴
    for i in range(1,s+1):
        nd = md[d]
        nx,ny = sx+nd[0]*i, sy+nd[1]*i
        if not check(nx,ny): break
        arr[nx][ny] = 0
    # 구슬 이동
    move()
    # 구슬 폭발
    while destroy():
        # 구슬 이동
        move()
    # 구슬 그룹별 새로운 번호(a,b 순) 부여
    new_number(arr)
print(1*b1+2*b2+3*b3)